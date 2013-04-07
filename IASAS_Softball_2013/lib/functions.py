def update_1B(): #increment singles
	batter = batter_number.get()
	old_singles = int(xml.singles(batter))
	xml.singles_w(batter, str(old_singles+1)) # write new value
	string = 'Single for %s - %s total' %(xml.name(batter), str(old_singles+1))
	console_log.set(string) #console log

def update_2B():
	batter = batter_number.get()
	old_doubles = int(xml.doubles(batter))
	xml.doubles_w(batter, str(old_doubles+1))
	string = 'Double for %s - %s total' %(xml.name(batter), str(old_doubles+1))
	console_log.set(string) #console log
	
def update_3B(): 
	batter = batter_number.get()
	old_triples = int(xml.triples(batter))
	xml.triples_w(batter, str(old_triples+1))
	string = 'Triple for %s - %s total' %(xml.name(batter), str(old_triples+1))
	console_log.set(string) #console log

def update_HR():
	batter = batter_number.get()
	old_homeruns = int(xml.homeruns(batter))
	xml.homeruns_w(batter, str(old_homeruns+1))
	string = 'Home run for %s - %s total' %(xml.name(batter), str(old_homeruns+1))
	console_log.set(string) #console log