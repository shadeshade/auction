import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from biddings.models import BiddingItem


class BidConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.bid_id = self.scope['url_route']['kwargs']['pk']
        self.room_group_name = 'bid_%s' % self.bid_id

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive bid_message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        bid_message = text_data_json['bid_message']
        current_price = text_data_json['current_price']

        new_bid = await self.place_bid(float(bid_message), float(current_price))
        if new_bid:
            # Send bid_message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'new_bid',
                    'bid_message': new_bid
                }
            )

    # Receive bid_message from room group
    async def new_bid(self, event):
        bid_message = event['bid_message']

        # Send bid_message to WebSocket
        await self.send(text_data=json.dumps({
            'bid_message': bid_message
        }))

    @database_sync_to_async
    def place_bid(self, bid, current_price):
        # obj: 'biddings.BiddingItem'
        # purchaser: 'users.MyUser'

        if bid > current_price:
            obj = BiddingItem.objects.get(id=self.bid_id)
            purchaser = self.scope['user']

            obj.price = bid
            obj.purchaser = purchaser
            obj.save()

            return bid
