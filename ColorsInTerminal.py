something = input('Please type something: ')

# STYLE
style0 = '\033[0m' + something + '\033[m'
style1 = '\033[1m' + something + '\033[m'
style2 = '\033[4m' + something + '\033[m'
style3 = '\033[7m' + something + '\033[m'

# TEXTCOLOR
color0 = '\033[0;30m' + something + '\033[m'
color1 = '\033[0;31m' + something + '\033[m'
color2 = '\033[0;32m' + something + '\033[m'
color3 = '\033[0;33m' + something + '\033[m'
color4 = '\033[0;34m' + something + '\033[m'
color5 = '\033[0;35m' + something + '\033[m'
color6 = '\033[0;36m' + something + '\033[m'
color7 = '\033[0;37m' + something + '\033[m'

# BAKCGROUNDCOLOR
colorBg0 = '\033[0;00;40m' + something + '\033[m'
colorBg1 = '\033[0;00;41m' + something + '\033[m'
colorBg2 = '\033[0;00;42m' + something + '\033[m'
colorBg3 = '\033[0;00;43m' + something + '\033[m'
colorBg4 = '\033[0;00;44m' + something + '\033[m'
colorBg5 = '\033[0;00;45m' + something + '\033[m'
colorBg6 = '\033[0;00;46m' + something + '\033[m'
colorBg7 = '\033[0;00;47m' + something + '\033[m'

print('-=-'*11)
print('  STYLE:')

print('{} | {} | {}'.format(style0, color0, colorBg0))
print('{} | {} | {}'.format(style1, color1, colorBg1))
print('{} | {} | {}'.format(style2, color2, colorBg2))
print('{} | {} | {}'.format(style3, color3, colorBg3))
print('{} | {} | {}'.format(style0, color4, colorBg4))
print('{} | {} | {}'.format(style0, color5, colorBg5))
print('{} | {} | {}'.format(style0, color6, colorBg6))
print('{} | {} | {}'.format(style0, color7, colorBg7))

print('-=-'*11)
