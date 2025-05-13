# [Reflections on Trusting Trust](https://www.archive.ece.cmu.edu/~ganger/712.fall02/papers/p761-thompson.pdf)

To what extent should one trust a statement of a program is free of Trojan horses? Perhaps it is more important to trust the people who wrote the software.

## Stage I

The problem is to write the shortest source program that, when compiled and executed, will produce as output an exact copy of its source.

It has to have two important properties:
1. This program can be easily written by another program
2. This program can contain an arbitrary amount of excess baggage that will be reproduced along with the main algorithm

```c
char s[] = {
	'\t',
	'0',
	'\n',
	'}',
	';',
	'\n',
	'\n',
	'/',
	'*',
	'\n',
	(213 lines deleted)
	0
}

/*
 * The string s is a
 * representation of the body
 * of this program from '0'
 * to the end.
 */

main()
{
	int i;
	
	printf("char\ts[] = {\n");
	for(i = 0; s[i]; i++)
		printf("\t%d, \n", s[i]);
	printf("%s", s);
} 
```

## Stage II

The C compiler is written in C. C allows individual characters in the string to be escaped to represent unprintable characters. For example

```c
	"Hello world\n"
```

It "knows" in a completely portable way what character code is compiled for a new line in a character set.

```c
c = next();
if(c != '\\')
	return(c);
c = next();
if(c == '\\')
	return('\\');
if(c == 'n')
	return('\n');
```

Suppose we wish to alter the C compiler to include `'\v'` to represent the vertical tab character. We must "train" the compiler. After it "knows" what `'\v'` means, then our new change will become legal C.

```c
c = next();
if(c != '\\')
	return(c);
c = next();
if(c == '\\')
	return('\\');
if(c == 'n')
	return('\n');
if(c == 'v')
	return('\v');
```

Now, the old compiler won't accept the new source. We look up on an ASCII chart that a vertical tab is decimal 11, we can alter our source code so the old compiler accepts the new source.

```c
c = next();
if(c != '\\')
	return(c);
c = next();
if(c == '\\')
	return('\\');
if(c == 'n')
	return('\n');
if(c == 'v')
	return(11);
```

You simply tell it once, then you can use this self-referencing definition.
