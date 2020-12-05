import guild

if __name__ == "__main__":
    niceg = guild.Guild.load('Nice Guild')

    print(niceg.level_up(niceg.hall))
    print(niceg.level_up(niceg.hall))

    print(niceg.level_up(niceg.hall))
    print(niceg.level_up(niceg.hall))

    print(niceg.level_up(niceg.hall))
    print(niceg.level_up(niceg.hall))
    
    niceg.save()