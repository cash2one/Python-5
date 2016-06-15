#include "python.h" 

static PyObject * 

spam_strlen(PyObject *self, PyObject *args)
{
    const char* str=NULL;
    int len; 

    // ��������Ʈ�� ���� �� �� �κ��� ������ ��.
    // �� ��ɻ� �ʿ��� �κ��� �ƴ϶�
    // �׳� �ƹ� ����̳� �־ c�� ������ ��.

    // PyArg_ParseTuple()
    // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
    // args�� s(string)���� str�� ��´�.
    if (!PyArg_ParseTuple(args, "s", &str))
         return NULL; 

    // ���ڿ��� ���̸� ���Ѵ�.
    len = strlen(str); 


    char temp[500];
    for (int i = 0; i < len; i++)
        temp[i] = str[len - i -1];
        temp[len] = '\0';


    // Py_BuildValue
    // ���ڿ��� ���̸� i(int)������ ��ȯ�Ѵ�.
    return Py_BuildValue("s", temp);
}
static PyMethodDef SpamMethods[] =
{
    { "strlen", spam_strlen, METH_VARARGS, "count a string length."}, 
    { NULL, NULL, 0, NULL                                          }  // �迭�� ���� ��Ÿ���ϴ�.
}; 
// ������ ��� ������ ��� ����ü
static struct PyModuleDef spammodule =
{
    PyModuleDef_HEAD_INIT,
    "spam",                // ������ ����Ʈ�� ��� �̸�
    "It is test module.",  // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
    -1,
    SpamMethods            // SpamMethods �迭����
};
PyMODINIT_FUNC
// ���̽� ���������Ϳ��� ó�� ����
// PyInit_<module> �Լ�
// spammodule�� �����.
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
