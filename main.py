text = '''However, the development team believed a change in drive format could enhance the flexibility of frame design and packaging. Therefore, the focus of research was to be to an underfloor, midship-engine rear-wheel drive (UMR) format. This could combine higher packaging efficiency along with the sporting characteristics with which rear drive was associated.
The potential in such a change also presented numerous obstacles. It was Honda’s first experience to design a car with the engine in the rear half of the vehicle. In February of the same year, with that in mind, and to expedite their research, the development team constructed a UMR test vehicle from a first-generation City.
During the test drive, the team members were amazed by the unique handling of the car, which differed greatly from the original FF specification. The UMR-version City, in fact, demonstrated superior performance characteristics. Unfortunately, further development had to be set aside because the level of technology then available to Honda placed certain limits on the car’s ability to present any real advantage over the normal FF version.
However, although the project was shelved, the team members simply could not forget the exhilaration they had experienced with the UMR experiment. Moreover, comments had been raised by supporters at the evaluation meetings that the rear-drive City’s dynamic performance should somehow be replicated.
The emphasis in research was therefore modified from drive format to dynamic performance - that which was typically achieved with a vehicle having a lower center of gravity, meaning a sportscar.
"It’s the dream of every development engineer to create a sportscar," said Shigeru Uehara, who was engaged in the development project as LPL. "The people who proposed changing the research direction at the evaluation meetings must also have had that dream."
In 1983, another step was taken, in the form of a prototype car fashioned from a CR-X as a means of testing dynamic performance from various perspectives. This was also the year Honda made its much-heralded return to the F-1 Series. Thus, of course, spirits were high at the R&D Center, in anticipation of the possibility that Honda might indeed build sportscars. Coincidentally, this had often been a subject of discussion at board meetings.
"I think the company wanted a car that could bridge its mass production FF models and F-1 cars," Uehara recalled. "They needed a car that would become the new face of Honda. Plus, we’d been contacted several times by those who were planning the Acura Division at American Honda concerning similar requests."
Honda’s development engineers finally found an outlet for the passions when in the fall of 1985 the creation of a new sportscar began in earnest.'''

positions_insensitive = [pos for pos, _ in enumerate(text.split()) if 'Honda' in _.lower()]
print("Позиции слова 'Honda' (любой регистр):", positions_insensitive)

import re
sentences = re.split(r'(?<=[.!?])\s+', text)
reversed_sentences = [sentence[::-1] for sentence in sentences]
for sentence in reversed_sentences:
    print(sentence)

delim_counts = {}
delimiters = [',', '.', '!', '?', '-', '(', ')']

for delimiter in delimiters:
    delimiter_positions = [pos for pos, char in enumerate(text) if char == delimiter]
    delimiter_count = len(delimiter_positions)
    delim_counts[delimiter] = {
        'positions': delimiter_positions,
        'count': delimiter_count
    }

for delimiter, data in delim_counts.items():
    print(f"Разделитель '{delimiter}':")
    print("Позиции:", data['positions'])
    print("Количество:", data['count'])
    print()




