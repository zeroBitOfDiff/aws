https://dev.to/byrro/crash-course-on-fan-out-fan-in-with-aws-lambda-47g0

response = client.invoke(
    FunctionName='string',
    InvocationType='Event'|'RequestResponse'|'DryRun',
    LogType='None'|'Tail',
    ClientContext='string',
    Payload=b'bytes'|file,
    Qualifier='string'
)