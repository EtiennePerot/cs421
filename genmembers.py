import urllib2, random, json, time

from library.people import *

possibleStreet1 = ('Sweet', 'Apple', 'Acres', 'Orange', 'Plum', 'Cumquats', 'Pear', 'Mango')
possibleStreet2 = ('Street', 'Avenue', 'Boulevard', 'Road', 'Highway')
possibleCitySuffix = ('ville', 'city', 'polis', 'town', 'country', '')
possibleNameConcat = ('', '_', '-', '.')
possibleEmailDomains = ('googlemail.com', 'yandex.ru', 'gmail.com', 'hotmail.com', 'live.com', 'yahoo.com', 'yahoo.ca', 'sogetthis.com', 'mailinator.com', 'inbox.com')
possibleRoles = ['Janitor', 'Librarian', 'Director', 'Reviewer', 'IT person', 'Manager thing']
possibleStanding = [Member.standing_good, Member.standing_bad]

def genName(first=True, last=True):
	j = json.load(urllib2.urlopen('http://thenamegenerator.com/api.php'))
	s = []
	if first:
		s.append(j['first_name'])
	if last:
		s.append(j['last_name'])
	return ' '.join(s)

def genAddress():
	streetNumber = str(random.randint(1, 9999))
	streetName = random.choice(possibleStreet1) + ' ' + random.choice(possibleStreet2)
	city = genName(first=False) + random.choice(possibleCitySuffix)
	return streetNumber + ' ' + streetName + ', ' + city

def genEmail(name):
	user = name.lower().replace(' ', random.choice(possibleNameConcat))
	if random.randint(0, 9) > 7: # With some probability, add a number to the username
		user += random.choice(possibleNameConcat) + str(random.randint(1, 2050))
	return user + '@' + random.choice(possibleEmailDomains)

def genPassword(name):
	# Because everyone uses their name as password; everybody knows that!
	# That's just common password hygiene.
	totallyRandomPassword = list(name.replace(' ', ''))
	random.shuffle(totallyRandomPassword)
	totallyRandomPassword = ''.join(totallyRandomPassword)
	if random.randint(0, 9) > 4: # Some silly people even try to make it more secure by adding numbers at the end
		totallyRandomPassword += random.choice(possibleNameConcat) * random.randint(1, 3) + str(random.randint(1, 2050))
	return totallyRandomPassword

if __name__ == '__main__':
	num = None
	while num is None:
		try:
			num = int(raw_input('How many people do you feel like creating today? '))
		except:
			print 'That\'s not a number. Try again, it\'s not very difficult.'
	for i in xrange(num):
		print 'Creating person', i + 1
		name = genName()
		address = genAddress()
		email = genEmail(name)
		password = genPassword(name)
		print 'Name:', name
		print 'Address:', address
		print 'Email:', email
		print 'Password:', password
		p = Person.create(name=name, address=address, email=email, password=password)
		if random.randint(0, 9) > 8: # With some probability, make it an employee
			role = random.choice(possibleRoles)
			salary = random.randint(100, 150000)
			employed = time.strftime('%Y-%m-%d', time.localtime(time.time() - random.randint(0, 3 * 365 * 24 * 3600)))
			print 'Role:', role
			print 'Salary: $' + str(salary)
			print 'Employed:', employed
			p.toEmployee(role, salary, employed)
		if random.randint(0, 9) > 4: # With some probability, make it a member
			standing = random.choice(possibleStanding)
			balance = random.randint(0, 999)
			expiration = time.strftime('%Y-%m-%d', time.localtime(time.time() + random.randint(1, 3 * 365 * 24 * 3600)))
			print 'Standing:', standing
			print 'Balance: $' + str(balance)
			print 'Expiration:', expiration
			p.toMember(standing, balance, expiration)
		print '--------------------------------------------'
