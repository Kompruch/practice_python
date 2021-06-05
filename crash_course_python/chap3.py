# friends = ['pond', 'ice', 'win']


# for name in friends:
#     print("Hello {}".format(name.title()))



# friends.remove('pond')

# print(friends)

# print('\n')
# for index in range(len(friends)):
#     print("Hello {}".format(friends[index].title()))

friends = ['pond', 'ice', 'win', 'jin', 'kim']

print(f'Good to see you, {friends[0].title()}. Let have a dinner.')

print('{} cannot come today. Then let find someone else'.format(friends[1].title()))
friends[1] = 'jane'


print('Nice to meet you all today {}, {}, {}, {}, and {}'.format(*friends))

print('Oh! I found a bigger table. Let invite more people')

friends.insert(0, 'adi')
friends.insert(2,'peach')
friends.append('louis')

for index, name in enumerate(friends):
    prev_person = index - 1
    if prev_person < 0:
        print(f'Thank you for comming {name}')
    else:
        print(f'Thank you for comming {name}. {friends[prev_person]} just comes')

while len(friends) > 2:
    pop_name = friends.pop()
    print(f'Sorry I have to cancel, {pop_name}')

print(f'Thanks for comming, {friends[0]}')
print(f'Thanks for comming, {friends[1]}')

del friends[0]
del friends[0]

print('The list is empty', friends)

