%module pthread

%{
#include "pthread.h"
%}

#define __attribute__(x)
#define __inline
#define __restrict
#define __extension__

%include "expanded.h";
