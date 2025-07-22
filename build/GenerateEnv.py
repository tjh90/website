import os
import re
import subprocess as sp

jdkVersionEnvVar = 'JDK_VERSION'

thisPath = os.path.dirname(os.path.realpath(__file__))
envFilename = os.path.join(thisPath, '.env')

########################################################################################################################

def getJdkVersion() -> str:
    result = sp.run(['java', '-XshowSettings:all', '-version'], capture_output=True, text=True).stderr

    lines = map (lambda l: l.strip(), result.splitlines())

    pattern = 'java.version'
    matcher = re.compile(pattern)
    versionLine = next(filter(lambda l: matcher.match(l), lines), None)
    if versionLine is not None:
        return versionLine.split('=')[1].strip().split('.')[0]

    return None

########################################################################################################################

if __name__ == '__main__':

    # If the .env file already exists, delete it.
    if os.path.exists(envFilename):
        os.remove(envFilename)

    # Determine the JDK version.
    jdkVersion = getJdkVersion()
    if not jdkVersion:
        raise ValueError('Failed to determine JDK version.')

    # Print the environment variables to the console.
    envVars = {
        jdkVersionEnvVar: jdkVersion,
    }
    print('Environment variables:')
    for (key, value) in envVars.items():
        print(f'    {key}={value}')

    # Write the environment variables to the .env file.
    with open(envFilename, 'w') as envFile:
        for (key, value) in envVars.items():
            envFile.write(f'{key}={value}\n'.format(key=key, value=value))
