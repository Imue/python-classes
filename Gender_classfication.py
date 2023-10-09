 
#Gender classification

sex = input ("Enter your sex: ").strip();

title = ''
if sex == 'm' or sex == 'male' :
    title = 'sir';
elif sex == 'f' or sex == 'female':
    title = 'Madam';
else:
    title = 'Sir/Madam';

print('Dear ',title)
input();
