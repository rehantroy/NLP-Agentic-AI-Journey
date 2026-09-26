letter = ''' Dear <|name|>,
            Your are selected!
            <|Date|>'''
update= letter.replace("<|name|>","Rehant").replace("<|Date|>","18 april 2025")

print(update)