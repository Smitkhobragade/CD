%{
 #include <stdio.h>
 #include <stdlib.h>
 %}
 %token ID NUMDOWHILELEGEEQNEORAND
 %right "="
 %left OR AND
 %left '>' '<' LE GE EQ NE
 %left '+' '-'
 %left '*' '/'
 %right UMINUS
 %left '!'
 %%
 S : ST {printf("Valid do while statement\n"); exit(0);}
 ST
 : DODEFWHILE'(' E ')'
 ;
 DEF : '{' BODY'}'
 | E';'
 | ST
 |
 ;
 BODY :BODYBODY
 | E ';'
 | ST
|
 ;
 E: ID '=' E
 | E '+' E
 | E '-' E
 | E '*' E
 | E '/' E
 | E '<' E
 | E '>' E
 | E LEE
 | E GEE
 | E EQE
 | E NEE
 | E ORE
 | E ANDE
 | E '+' '+'
 | E '-' '-'
 | ID
 | NUM
 ;
 %%
 main() {
 printf("Enter the do while statement to check :");
 yyparse();
 }

 int yywrap(void)
 {
     return 1;
 }


 int yyerror(char *mes) {
 printf("Invalid do while statement\n");
 return 0;
 }
