%{
#include "y.tab.h"
extern int yylval;
%}
%%
[0-9]+ {yylval=atoi(yytext); return NUMBER;}
[a-zA-Z]* {yylval=strdup(yytext);return ID;}
\n {return NL;}
. {return yytext[0];}
%%


