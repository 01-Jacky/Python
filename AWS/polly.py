import boto3
import os

AWS_POLLY_US_WEST_2 = {
    'region_name' : 'us-west-2',
    'aws_access_key_id' : os.environ['aws_access_key_id'],
    'aws_secret_access_key' : os.environ['aws_secret_access_key'],
}


def connectToPolly(aws_params):
    # client vs resource?
    # polly = boto3.resource('polly', **AWS_POLLY_US_WEST_2)
    return boto3.client('polly', **aws_params)


def get_text():
    pass


def generate_speech(polly, text, format='mp3', voice='Joanna'):
    resp = polly.synthesize_speech(OutputFormat=format, Text=text, VoiceId=voice)
    bytestream = resp['AudioStream'].read()
    return bytestream


def save_speech_local(bytestream):
    soundfile = open('tmp/sound.mp3', 'wb')
    soundfile.write(bytestream)
    soundfile.close()
    return True

def save_speech_s3()


sample_message = "Hello world. This is a test of AWS Polly"

print("Connecting to AWS Polly")
polly = connectToPolly(AWS_POLLY_US_WEST_2)
bytestream = generate_speech(polly, sample_message)

print("Recieved audio byte stream. Saving...")
save_speech(bytestream)
print("Saved in directory tmp")

