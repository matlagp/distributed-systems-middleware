import sys
import asyncio
import grpc
import time
import eventify_pb2 as eventify
import eventify_pb2_grpc as eventify_grpc

async def subscribe_to_type(stub, type_name):
    subscription_string = "Subscribed: %s" % type_name
    print(subscription_string)
    print("-" * len(subscription_string))

    reconnect_interval = 1
    request = eventify.SubRequest(type=string_to_event_type(type_name))

    while True:
        try:
            events = stub.Subscribe(request)

            for event in events:
                print("New %s event: %s" % (type_name, event))
                reconnect_interval = 1  # Got connection, reset timer
        except grpc.RpcError as e:
            print("Connectivity issue: %s" % e.details())
            time.sleep(reconnect_interval)
            reconnect_interval = increase_interval(reconnect_interval)

def string_to_event_type(type_name):
    event_types = {
        "CONCERT": eventify.EventType.CONCERT,
        "CONFERENCE": eventify.EventType.CONFERENCE,
        "FESTIVAL": eventify.EventType.FESTIVAL
    }

    return event_types[type_name.upper()]

def increase_interval(interval):
    new_interval = interval * 2
    if new_interval > 30:
        new_interval = 30

    return new_interval

async def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = eventify_grpc.EventifyStub(channel)
        coroutines = []
        for event_type in sys.argv[1:]:
            coroutines.append(subscribe_to_type(stub, event_type))

        await asyncio.gather(*coroutines)

if __name__ == '__main__':
    asyncio.run(main())