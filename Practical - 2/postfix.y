%{
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char postfix[100];
int pos = 0;
%}

%token NUMBER ID NL
%left '+' '-'
%left '*' '/'

%%
stmt : exp NL {
    printf("The Entered expression is valid.\n");
    printf("Postfix Expression: %s\n", postfix);
    exit(0);
}
|
 exp1 NL {
    printf("The Entered expression is valid.\n");
    printf("Postfix exp : %s\n",postfix);
    exit(0);
}
;

exp : exp '+' exp   {$$=$1+$3; sprintf(postfix + pos, "%c", '+'); pos++;}
| exp '-' exp {$$=$1-$3; sprintf(postfix + pos, "%c", '-'); pos++;}
| exp '*' exp {$$=$1*$3; sprintf(postfix + pos, "%c", '*'); pos++;}
| exp '/' exp {$$=$1/$3; sprintf(postfix + pos, "%c", '/'); pos++;}
| '(' exp ')' {$$=$2;}
| NUMBER {$$=$1; sprintf(postfix + pos, "%d", $1); pos += strlen(postfix + pos);}
;

exp1 : exp1 '+' exp1  {$$=$1+$3; sprintf(postfix + pos, "%c", '+'); pos++;}
| exp1 '-' exp1       {$$=$1-$3; sprintf(postfix + pos, "%c", '-'); pos++;}
| exp1 '*' exp1       {$$=$1*$3; sprintf(postfix + pos, "%c", '*'); pos++;}
| exp1 '/' exp1       {$$=$1/$3; sprintf(postfix + pos, "%c", '/'); pos++;}
| '(' exp1 ')'        {$$=$2;}
| ID     {$$=$1; sprintf(postfix + pos, "%s", $1); pos += strlen(postfix + pos);}
; 

%%
int yyerror(char *msg)
{
    printf("Invalid Expression\n");
    exit(0);
}

int main()
{
    printf("Enter the expression: \n");
    yyparse();
    return 0;
}

int yywrap()
{
    return 1;
}