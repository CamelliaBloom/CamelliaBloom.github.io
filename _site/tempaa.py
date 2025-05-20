

str1 = """any time	Fellowship	RElevate (High School)	future Leader	Fri 7:00-9:00	OLDIE (Observe, Learn, Do; then Inspire and Encourage others)	green
any time	Misc	Website	Webmaster	any	design and update (for information and communication)	green
any time	Misc	Care and Connection Team (CCT)	Designer	any	creatively design physical spaces for best balance between beauty, function and safety	green
any time	Sunday School	IMPACT (Adults)	Leader/Facilitator	Sun 11:00-12:00	OLDIE (Observe, Learn, Do; then Inspire and Encourage others)	green
any time	Worship Service	Audio-Visual Team (AV)	Sound and/or PPT Operator	Sun 9:30-10:45	run sound mixer and/or Powerpoint; cast via OBS software to Youtube	green
any time	Worship Service	Worship Team (WS)	Vocalist, Instrumentalist	Sun 9:30-10:45	lead congregation in worshipping God through music	green
any time	Worship Service		Chairperson	Sun 9:30-10:45	MC (in the absence of other roles: welcome people, announcements, Scripture Reading)	black
any time	Worship Service		Holy Communion Server	Sun 9:30-10:45	prepare and/or pray for/serve Holy Communion (1st Sundays)	black
any time	Worship Service		Scripture Reader	Sun 9:30-10:45	read Scripture (in-person or via Zoom); spoken, visual (drama, etc.)	black
any time	Worship Service		Setup/Attendance	Sun 8:45-10:45	various tasks to get Sanctuary and Classrooms ready	black
any time	Worship Service		Visitor Follow-Up	any	follow up with Visitors during week	black
any time	AWANA		Teacher, Group Leader	Fri 7:00-9:00	take turns in lesson teaching and/or lead students in small group work and discussion and prayer for one another	black
any time	Sunday School	Children (up to Grade 6)	Teachers, Helpers	Sun 9:30-10:45	take turns in lesson teaching and/or lead students in small group work and discussion and prayer for one another	blue
"""

for line in str1.splitlines("\n"):
    lst = line.split("\t")
    # print(lst)
    color = lst[-1].strip("\n")
    print(f'  <tr class="tooltip-hover" data-tooltip="{lst[-2]}">')
    for ll in lst[:-2]:
        print(f'    <td><span class="color-{color}">{ll}</span></td>')

    print("  </tr>")
    