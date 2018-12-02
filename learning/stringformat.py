#Old
#'%s %s' % ('one', 'two')
#New
#'{} {}'.format('one', 'two')


print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two'))
print('{1} {0} {0}'.format('one','two'))

day=0
is_weekend = day == 0 or day == 6

print(is_weekend)