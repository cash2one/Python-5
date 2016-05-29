#include "python.h" 

static PyObject * 

spam_strlen(PyObject *self, PyObject *args)
{
    const char* str=NULL;
    int len; 

    // 텀프로젝트에 넣을 땐 이 부분을 수정할 것.
    // 꼭 기능상 필요한 부분이 아니라도
    // 그냥 아무 기능이나 넣어서 c와 연동할 것.

    // PyArg_ParseTuple()
    // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
    // args을 s(string)으로 str에 담는다.
    if (!PyArg_ParseTuple(args, "s", &str))
         return NULL; 

    // 문자열의 길이를 구한다.
    len = strlen(str); 


    char temp[500];
    for (int i = 0; i < len; i++)
        temp[i] = str[len - i -1];
        temp[len] = '\0';


    // Py_BuildValue
    // 문자열의 길이를 i(int)형으로 반환한다.
    return Py_BuildValue("s", temp);
}
static PyMethodDef SpamMethods[] =
{
    { "strlen", spam_strlen, METH_VARARGS, "count a string length."}, 
    { NULL, NULL, 0, NULL                                          }  // 배열의 끝을 나타냅니다.
}; 
// 생성할 모듈 정보를 담는 구조체
static struct PyModuleDef spammodule =
{
    PyModuleDef_HEAD_INIT,
    "spam",                // 실제로 임포트할 모듈 이름
    "It is test module.",  // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
    -1,
    SpamMethods            // SpamMethods 배열참조
};
PyMODINIT_FUNC
// 파이썬 인터프리터에서 처음 실행
// PyInit_<module> 함수
// spammodule을 만든다.
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
