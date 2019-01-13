%module pthread

%{
#include "pthread.h"
%}

%include "swig_helper.i";

%rename("$ignore", regextarget=1) "^_";

%include "expanded.h";
