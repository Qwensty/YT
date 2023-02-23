from utils.channel import Channel


def main():

    #channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
    channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'    # Редакция

    channel = Channel(channel_id)
    channel.print_info()

    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    vdud.print_info()


if __name__ == "__main__":
    main()
