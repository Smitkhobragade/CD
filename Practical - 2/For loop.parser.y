%{
#include <stdio.h>
#include <stdlib.h>
%}

%token ID NUM FOR LE GE EQ NE OR AND ';'
%right '='
%left '+' '-'
%left '*' '/'
%left UNARY

%%

S         : FOR '(' E ';' E ';' E ')' '{' STMTS '}' { printf("Valid for loop statement\n"); }
          ;

STMTS     : STMTS STMT
          | /* empty */
          ;

STMT      : S
          | ID '=' E ';'
          | ';'
          ;

E         : ID '=' E
          | E '+' E
          | E '-' E
          | E '*' E
          | E '/' E
          | ID
          | NUM
          | E '<' E
          | E '>' E
          | E LE E
          | E GE E
          | E EQ E
          | E NE E
          | E OR E
          | E AND E
          | '(' E ')' %prec UNARY
          ;

%%

int main() {
    printf("Enter the for loop statement to check: ");
    yyparse();
    return 0;
}

int yywrap(void) {
    return 1;
}

int yyerror(char *mes) {
    printf("Invalid statement\n");
    return 0;
}
