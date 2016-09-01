# antipep8
This script may convert python source from pep8 to better styles.

What is a better style? People may have different answer. For me, the spaces in parenthese or braces are necessary, with which I can find the other parenthesis or brace quickly.

So, I don't like pep8 code style. Unfortunately, the leaders in many companies prefer pep8. Only because it is well known. They want to make everyone's code look samilar. They are mindless of the style itself. To be pretty is nothing. To be ugly is ok. All what important is to coincide with each other. Do you know the North Korea's group calisthenics? Many person act as one. Every dictator dreams it. 

When flake8 is pressed to my git, I can not add a space that offends pep8. It raises an error utterly discomfited just for a space to make the code looks better. I have to convert the code with autopep8 to fit the emperor's taste. Then push it to the remote repo without a glance.

And how to get it back? Now, I write a tool to convert code from pep8 to better styles. For me, a better style is to add spaces in parenthese and braces.

f(a, b, c) #bad

f( a, b, c ) #good

f( ( a, ), b ) #bad

f(( a, ), b ) #good

I can covert the code to my style after pulling, edit it happily, convert it back and throw it to the leaders. Problems are solved. Life is good.
