import pkg_resources, subprocess, sys

required  = {'vpython','keyboard', 'easygui'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing   = required - installed

if missing:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])