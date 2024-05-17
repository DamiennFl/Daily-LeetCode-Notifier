import asyncio


class MySMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print(f"Received message from: {envelope.mail_from}")
        print(f"To: {envelope.rcpt_tos}")
        print("Message data:")
        print(envelope.content.decode("utf-8"))
        return "250 Message accepted for delivery"


if __name__ == "__main__":
    controller = Controller(MySMTPHandler(), hostname="localhost", port=8025)
    controller.start()
    print("SMTP server running...")
    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("SMTP server stopped.")
        controller.stop()
