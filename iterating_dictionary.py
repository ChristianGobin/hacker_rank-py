#!/usr/bin/env python3

random_dict = {
	'users' : ['mark', 'john', 'victor', 'james', 'tony'],
	'speed' : 'slow',
	'average' : 22.01
}

print(random_dict.items())
for item in random_dict['users']:
	print(item.capitalize())