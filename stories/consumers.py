from channels.generic.websocket import AsyncWebsocketConsumer
import json




class TrackElectionComsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print("Connection.....")
        electionId = self.scope['url_route']['kwargs']['id'] 
        print("Election ID: ", electionId)
        self.election_id = electionId
        print("self.election_id: ", self.election_id)
        self.room_group_name = f'tracking-election-{electionId}'
        print("self.room_group_name: ", self.room_group_name)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        
        print(f"Connection disconnected with  code: {close_code}")

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):

        data_json = json.loads(text_data)
        party = data_json['party']
        voter = data_json['voter']


        print(f"{voter} voted {party} in the election")

        await self.send(text_data=json.dumps({
            'voter': f'{voter} -- from the server',
            'party': party
        }))



