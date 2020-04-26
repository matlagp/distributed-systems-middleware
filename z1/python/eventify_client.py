import sys
import asyncio
import grpc
import eventify_pb2 as eventify
import eventify_pb2_grpc as eventify_grpc

async def subscribe_to_type(stub, type_name):
    subscription_string = "Subscribed: %s" % type_name
    print(subscription_string)
    print("-" * len(subscription_string))

    request = eventify.SubRequest(type=string_to_event_type(type_name))

    events = stub.Subscribe(request)

    for event in events:
        print("New %s event: %s" % (type_name, event))

def string_to_event_type(type_name):
    event_types = {
        "CONCERT": eventify.EventType.CONCERT,
        "CONFERENCE": eventify.EventType.CONFERENCE,
        "FESTIVAL": eventify.EventType.FESTIVAL
    }

    return event_types[type_name.upper()]

async def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = eventify_grpc.EventifyStub(channel)
        print(sys.argv[1:])
        coroutines = []
        for event_type in sys.argv[1:]:
            coroutines.append(subscribe_to_type(stub, event_type))

        await asyncio.gather(*coroutines)

if __name__ == '__main__':
    asyncio.run(main())