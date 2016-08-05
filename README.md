# antipep8
This script may convert python source from pep8 to better styles.

What is a better style? People may have different answer. For me, the spaces in parenthese and braces are necessary, with which I can find the other parenthesis quickly.

So, I don't like pep8 code style. Unfortunately, the leaders in many companies wants pep8. Only because it is widely known. They want to make everyone's code look samilar. They are mindless of the style itself. To be pretty is nothing. To be ugly is ok. All what important is to coincide with each other. Do you know the North Korea's group calisthenics? Many person act as one. Every dictator dreams. 

When flake8 is pressed to my git, I can not add a space that offends pep8. It raises a error just for a space to make the code looks better. I have to convert the code with autopep8. After converting I throw it to the remote repo without a glance.

Now, I write a tool to convert code from pep8 to better styles. For me, it is to add spaces in parenthese and braces.

f(a, b, c) #bad
f( a, b, c ) #good
f( ( a, ), b ) #bad
f(( a, ), b ) #good

I can covert the code to my style after pulling, edit it happily, and convert it back and throw it away. Problems are solved. Life is good.
