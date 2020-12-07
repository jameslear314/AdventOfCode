import math
INPUT = '''shiny plum bag contain 0 other bag
clear crimson bag contain 3 pale aqua bag, 4 plaid magenta bag, 3 dotted beige bag, 3 dotted black bag
dim violet bag contain 5 bright brown bag
mirrored tomato bag contain 3 faded maroon bag, 3 dark green bag
muted salmon bag contain 1 posh yellow bag
posh lime bag contain 1 dim lavender bag
light fuchsia bag contain 5 faded coral bag
plaid lime bag contain 1 dull brown bag, 4 clear black bag, 3 dotted coral bag
dim crimson bag contain 2 striped blue bag
drab salmon bag contain 3 plaid fuchsia bag, 1 mirrored teal bag, 4 posh aqua bag
dark red bag contain 1 bright magenta bag, 1 posh lavender bag, 2 dark gray bag, 1 wavy lime bag
striped indigo bag contain 2 drab brown bag
vibrant beige bag contain 3 drab gray bag, 4 shiny gold bag, 4 dull white bag, 3 bright lavender bag
pale maroon bag contain 1 pale crimson bag, 2 mirrored magenta bag
dull cyan bag contain 4 mirrored green bag, 2 striped red bag, 1 clear blue bag, 5 muted gold bag
clear brown bag contain 3 light orange bag, 2 striped red bag
wavy white bag contain 3 bright purple bag, 2 posh lime bag, 1 faded crimson bag
shiny green bag contain 4 dim red bag, 3 vibrant blue bag, 2 dotted plum bag
dotted indigo bag contain 5 muted lime bag, 2 drab maroon bag, 2 bright tomato bag
muted purple bag contain 3 pale chartreuse bag, 2 dim plum bag, 2 striped blue bag
dotted magenta bag contain 1 mirrored maroon bag, 3 shiny red bag, 2 faded blue bag, 2 mirrored purple bag
posh maroon bag contain 4 dull olive bag, 3 dark blue bag
pale teal bag contain 4 posh lavender bag, 5 light lavender bag, 5 clear violet bag
faded red bag contain 2 dotted lime bag
bright lime bag contain 1 dim blue bag
vibrant gold bag contain 4 dark violet bag, 1 faded crimson bag
shiny cyan bag contain 5 clear beige bag, 1 wavy cyan bag
shiny crimson bag contain 4 posh salmon bag, 5 dim fuchsia bag
striped salmon bag contain 1 striped lime bag
faded silver bag contain 5 dull blue bag
dull crimson bag contain 1 dark bronze bag
dull silver bag contain 5 light purple bag, 2 dim crimson bag, 2 plaid red bag
vibrant plum bag contain 2 mirrored indigo bag, 4 pale chartreuse bag, 2 muted violet bag
muted green bag contain 2 dull black bag, 1 mirrored green bag
vibrant crimson bag contain 5 dark beige bag, 5 dull maroon bag, 5 drab lavender bag
drab orange bag contain 2 posh silver bag, 2 dim olive bag, 1 plaid green bag
striped silver bag contain 3 shiny indigo bag
plaid bronze bag contain 2 dull silver bag
striped yellow bag contain 4 dim tomato bag
plaid beige bag contain 1 striped black bag, 2 wavy purple bag, 4 striped blue bag
mirrored blue bag contain 1 dim green bag, 5 dark maroon bag, 5 plaid plum bag
pale green bag contain 1 mirrored aqua bag, 2 mirrored indigo bag, 4 vibrant red bag
plaid gold bag contain 4 wavy magenta bag
vibrant olive bag contain 5 mirrored magenta bag, 1 plaid salmon bag, 3 bright white bag
bright teal bag contain 5 bright fuchsia bag
drab purple bag contain 3 muted lavender bag, 2 plaid gold bag, 5 muted green bag, 3 drab gold bag
mirrored lime bag contain 3 light orange bag, 3 dim chartreuse bag, 5 shiny brown bag
faded plum bag contain 3 light orange bag, 5 dotted orange bag, 2 striped bronze bag, 3 light aqua bag
plaid indigo bag contain 5 bright cyan bag
shiny blue bag contain 4 drab turquoise bag
bright crimson bag contain 5 clear cyan bag, 2 pale maroon bag, 3 muted lavender bag
dark purple bag contain 2 shiny brown bag, 1 posh aqua bag, 2 wavy gold bag, 4 mirrored teal bag
striped crimson bag contain 3 shiny brown bag
light crimson bag contain 5 dark white bag, 2 shiny lavender bag, 1 muted white bag
dark violet bag contain 3 muted violet bag, 1 bright green bag, 2 dotted maroon bag
striped white bag contain 1 light coral bag, 2 light brown bag
dotted beige bag contain 5 light coral bag, 3 plaid black bag, 1 bright lavender bag, 5 posh green bag
plaid plum bag contain 0 other bag
striped red bag contain 3 plaid green bag
light white bag contain 5 plaid teal bag, 5 faded tan bag
clear purple bag contain 1 drab cyan bag, 2 shiny fuchsia bag, 4 dull beige bag
clear beige bag contain 4 dim cyan bag, 4 clear gold bag
clear indigo bag contain 2 faded beige bag, 5 shiny gold bag, 1 dark brown bag
plaid coral bag contain 1 striped black bag
wavy cyan bag contain 1 posh coral bag, 2 shiny black bag
striped green bag contain 1 pale green bag, 1 striped red bag, 5 striped tomato bag, 4 clear tomato bag
shiny salmon bag contain 1 bright silver bag, 1 faded gray bag, 1 muted lime bag, 5 vibrant chartreuse bag
pale gray bag contain 1 drab gray bag
vibrant tomato bag contain 5 dim turquoise bag, 1 pale blue bag, 2 striped brown bag, 3 plaid red bag
dotted red bag contain 4 plaid black bag, 3 dotted blue bag
faded aqua bag contain 1 striped turquoise bag, 1 dark tan bag
wavy silver bag contain 5 pale cyan bag
faded salmon bag contain 2 clear salmon bag, 1 plaid green bag, 2 shiny white bag, 1 pale chartreuse bag
dull turquoise bag contain 1 clear violet bag
plaid magenta bag contain 4 wavy cyan bag
vibrant maroon bag contain 3 plaid plum bag
striped turquoise bag contain 2 shiny lavender bag, 2 light aqua bag, 5 drab magenta bag
wavy crimson bag contain 4 posh coral bag, 1 wavy lime bag, 1 plaid plum bag, 4 dull maroon bag
wavy red bag contain 5 vibrant blue bag
plaid silver bag contain 4 light salmon bag, 5 faded indigo bag, 3 clear magenta bag
wavy salmon bag contain 5 dim olive bag, 3 posh magenta bag, 4 dark turquoise bag, 5 drab teal bag
dark yellow bag contain 2 drab silver bag, 3 dim cyan bag, 3 clear olive bag, 3 dotted crimson bag
striped brown bag contain 5 clear gray bag, 3 wavy salmon bag
posh lavender bag contain 4 light teal bag, 4 wavy turquoise bag, 1 dim yellow bag
muted beige bag contain 4 dull teal bag
vibrant purple bag contain 5 dark silver bag, 2 striped gold bag
bright yellow bag contain 2 dark blue bag, 2 bright brown bag
dim tan bag contain 3 striped lime bag, 4 posh silver bag, 3 drab teal bag, 4 mirrored magenta bag
drab chartreuse bag contain 3 shiny brown bag, 5 dark silver bag, 4 muted olive bag
clear maroon bag contain 4 clear indigo bag
posh orange bag contain 3 light silver bag, 3 clear black bag, 1 faded maroon bag, 5 wavy red bag
plaid chartreuse bag contain 2 vibrant beige bag, 1 dull aqua bag, 3 clear blue bag, 2 wavy fuchsia bag
dull beige bag contain 3 mirrored black bag, 4 drab gray bag
clear fuchsia bag contain 1 posh olive bag, 4 wavy silver bag, 1 faded beige bag
dim blue bag contain 4 muted lavender bag, 2 mirrored black bag, 5 dull white bag
faded coral bag contain 5 drab teal bag, 2 plaid green bag
shiny fuchsia bag contain 2 striped coral bag
mirrored green bag contain 5 bright purple bag, 1 dim olive bag, 1 dark green bag
muted gray bag contain 2 bright white bag, 4 mirrored turquoise bag, 4 plaid teal bag
plaid blue bag contain 3 mirrored indigo bag
bright maroon bag contain 5 vibrant aqua bag
dark magenta bag contain 1 dull crimson bag, 3 clear orange bag, 2 plaid chartreuse bag
dark coral bag contain 4 dull green bag
wavy plum bag contain 3 plaid plum bag, 5 drab lavender bag
faded indigo bag contain 4 shiny brown bag, 5 dotted salmon bag, 3 vibrant aqua bag
dotted tomato bag contain 1 vibrant plum bag
bright violet bag contain 4 dim yellow bag, 3 dark silver bag, 5 posh beige bag, 5 wavy lavender bag
shiny chartreuse bag contain 3 bright brown bag, 2 dim cyan bag, 4 shiny brown bag, 1 clear black bag
dim chartreuse bag contain 0 other bag
bright turquoise bag contain 3 clear lime bag, 3 clear violet bag, 2 dotted maroon bag, 1 dark cyan bag
plaid salmon bag contain 3 dark tomato bag, 5 light maroon bag
drab tan bag contain 2 light tomato bag, 4 clear maroon bag, 1 dim olive bag, 5 dark teal bag
dim green bag contain 3 muted aqua bag, 3 mirrored aqua bag
drab yellow bag contain 1 clear chartreuse bag
clear lavender bag contain 1 wavy salmon bag, 3 dull tan bag, 5 plaid magenta bag
mirrored magenta bag contain 5 dark violet bag
dotted white bag contain 2 muted blue bag, 1 light brown bag, 1 bright red bag, 3 posh aqua bag
faded black bag contain 1 light violet bag, 5 muted aqua bag, 4 striped blue bag, 2 dull gray bag
bright plum bag contain 3 dull white bag, 3 wavy maroon bag
light gray bag contain 1 posh magenta bag
dull orange bag contain 4 dotted chartreuse bag, 2 clear lavender bag, 4 pale silver bag, 5 shiny blue bag
wavy purple bag contain 3 striped orange bag, 2 light aqua bag, 5 dull blue bag, 3 striped lime bag
plaid green bag contain 1 dotted blue bag
plaid purple bag contain 1 drab aqua bag, 4 dark bronze bag, 1 vibrant olive bag
bright green bag contain 4 dim green bag, 2 dull aqua bag, 1 striped orange bag, 3 light teal bag
posh cyan bag contain 5 pale orange bag, 5 faded chartreuse bag
posh white bag contain 1 dark cyan bag, 1 dark magenta bag, 2 pale plum bag, 2 striped teal bag
mirrored red bag contain 1 dotted violet bag, 4 dotted white bag, 4 faded tan bag, 4 wavy maroon bag
dim turquoise bag contain 2 dark brown bag
vibrant fuchsia bag contain 4 muted aqua bag, 1 light maroon bag
light turquoise bag contain 5 bright cyan bag, 2 pale cyan bag
striped coral bag contain 3 striped turquoise bag, 1 posh green bag, 1 dark brown bag
dim black bag contain 2 posh coral bag
mirrored orange bag contain 3 dull maroon bag, 5 bright purple bag, 2 striped turquoise bag
clear cyan bag contain 5 wavy green bag, 4 faded coral bag, 4 muted purple bag
muted aqua bag contain 0 other bag
drab maroon bag contain 1 vibrant orange bag, 5 dotted white bag
dim brown bag contain 1 dark plum bag, 5 light aqua bag, 5 striped orange bag, 3 vibrant aqua bag
dim teal bag contain 3 pale gold bag, 4 dark teal bag
pale white bag contain 2 shiny lavender bag, 2 clear gray bag, 3 pale purple bag, 5 striped yellow bag
wavy black bag contain 5 wavy red bag, 2 vibrant bronze bag
posh brown bag contain 4 shiny cyan bag
bright bronze bag contain 2 plaid black bag, 3 mirrored gold bag, 4 drab silver bag, 4 striped orange bag
shiny silver bag contain 5 muted gold bag, 4 light blue bag
bright indigo bag contain 2 dotted gold bag, 5 vibrant red bag, 5 faded olive bag, 4 mirrored purple bag
shiny violet bag contain 3 mirrored black bag, 2 bright maroon bag, 2 vibrant gold bag
plaid crimson bag contain 1 plaid beige bag
pale tomato bag contain 2 dark tomato bag
striped bronze bag contain 5 bright magenta bag
wavy violet bag contain 4 drab gray bag
faded crimson bag contain 2 plaid plum bag, 5 vibrant aqua bag, 5 posh yellow bag, 4 bright lavender bag
shiny aqua bag contain 4 faded silver bag, 2 dark maroon bag
light lavender bag contain 3 dim chartreuse bag
wavy orange bag contain 1 striped lime bag, 3 mirrored indigo bag, 2 vibrant plum bag, 4 dull tomato bag
posh aqua bag contain 2 posh magenta bag
pale black bag contain 2 drab green bag, 4 wavy olive bag, 4 plaid teal bag, 3 posh silver bag
dotted crimson bag contain 1 pale gold bag, 5 dark brown bag, 4 dull aqua bag
light orange bag contain 4 plaid green bag
drab silver bag contain 5 wavy tan bag, 5 plaid tomato bag, 2 vibrant violet bag, 3 pale chartreuse bag
vibrant red bag contain 4 light aqua bag, 4 striped orange bag, 5 dark blue bag, 3 faded green bag
wavy olive bag contain 3 dull beige bag, 2 dim lavender bag, 1 striped gold bag
dull tomato bag contain 3 vibrant violet bag, 1 shiny chartreuse bag, 4 plaid beige bag, 2 clear indigo bag
dull coral bag contain 3 bright green bag, 4 dim purple bag
faded magenta bag contain 3 drab olive bag, 2 faded maroon bag, 3 striped blue bag
plaid yellow bag contain 1 faded brown bag, 1 faded gold bag, 5 drab fuchsia bag
pale crimson bag contain 5 drab silver bag, 2 striped crimson bag
plaid red bag contain 4 vibrant aqua bag
vibrant bronze bag contain 4 shiny aqua bag
muted crimson bag contain 3 vibrant chartreuse bag, 3 shiny fuchsia bag, 2 dull fuchsia bag, 4 striped brown bag
bright lavender bag contain 4 muted aqua bag, 3 dim green bag
dotted silver bag contain 1 striped white bag, 5 dark magenta bag, 2 clear green bag, 3 dim silver bag
mirrored olive bag contain 5 drab turquoise bag, 2 dim orange bag, 5 dark aqua bag, 4 posh plum bag
pale blue bag contain 2 posh green bag, 5 shiny lavender bag, 1 dim brown bag, 5 drab magenta bag
striped purple bag contain 5 vibrant beige bag, 3 vibrant bronze bag
wavy green bag contain 5 plaid plum bag, 2 muted blue bag, 5 drab gray bag, 2 posh magenta bag
clear aqua bag contain 5 wavy green bag, 5 wavy maroon bag, 3 plaid salmon bag, 4 dark salmon bag
striped aqua bag contain 4 mirrored purple bag
pale lime bag contain 3 dull blue bag
vibrant orange bag contain 5 light brown bag, 4 posh silver bag
pale brown bag contain 4 striped yellow bag, 1 light salmon bag, 2 dark blue bag
bright magenta bag contain 2 wavy cyan bag
clear tan bag contain 5 dark gold bag
pale beige bag contain 4 vibrant orange bag, 2 posh tomato bag
mirrored gray bag contain 4 dull salmon bag
faded lime bag contain 3 muted purple bag, 4 clear lime bag
dark fuchsia bag contain 4 dull crimson bag, 1 vibrant cyan bag, 2 light lavender bag, 1 dark tomato bag
shiny teal bag contain 3 mirrored tomato bag, 3 plaid coral bag, 2 shiny coral bag
wavy magenta bag contain 1 vibrant cyan bag, 1 posh green bag, 4 vibrant aqua bag
dotted bronze bag contain 1 clear orange bag, 2 dull lavender bag, 2 clear salmon bag
plaid gray bag contain 1 shiny brown bag, 1 plaid turquoise bag, 3 faded silver bag, 2 mirrored white bag
dark tan bag contain 1 light lavender bag
bright orange bag contain 2 wavy gray bag
light yellow bag contain 4 light blue bag, 3 muted blue bag, 1 plaid red bag, 3 mirrored aqua bag
faded maroon bag contain 2 shiny brown bag, 4 drab magenta bag, 2 dotted maroon bag, 5 mirrored indigo bag
dark aqua bag contain 2 bright gold bag, 3 plaid tomato bag
striped gray bag contain 4 dark tomato bag
bright olive bag contain 1 light gold bag, 4 faded coral bag, 5 dark brown bag, 4 faded maroon bag
mirrored yellow bag contain 5 shiny silver bag, 5 dull violet bag, 5 drab silver bag, 5 pale lavender bag
shiny gold bag contain 3 posh green bag, 2 dull white bag
pale aqua bag contain 1 vibrant cyan bag, 2 posh gray bag, 3 faded beige bag, 2 dark gold bag
light bronze bag contain 4 dotted black bag, 4 bright lavender bag, 2 plaid maroon bag
plaid cyan bag contain 3 vibrant turquoise bag
dull black bag contain 3 muted violet bag, 2 shiny brown bag, 4 dim chartreuse bag, 1 light lavender bag
dotted brown bag contain 1 shiny white bag, 5 muted blue bag, 5 pale white bag, 3 bright gray bag
clear turquoise bag contain 4 dark blue bag, 3 drab gold bag
mirrored salmon bag contain 1 posh aqua bag, 2 dark gold bag, 4 dull black bag
drab blue bag contain 2 plaid red bag, 3 wavy chartreuse bag, 3 posh salmon bag
pale purple bag contain 1 wavy tan bag, 5 shiny lavender bag, 4 faded beige bag
shiny lavender bag contain 2 dim olive bag, 3 vibrant aqua bag, 1 shiny plum bag, 1 dim cyan bag
plaid brown bag contain 3 faded black bag, 5 wavy violet bag, 5 faded white bag
faded tan bag contain 4 clear tan bag, 4 clear gold bag
dim cyan bag contain 4 vibrant lime bag, 5 faded silver bag, 4 pale lime bag, 2 dim chartreuse bag
vibrant green bag contain 5 plaid blue bag, 3 shiny maroon bag, 4 dotted violet bag
drab turquoise bag contain 2 drab gray bag, 5 clear magenta bag
bright coral bag contain 4 clear gold bag, 4 light coral bag
shiny yellow bag contain 5 shiny chartreuse bag, 2 wavy green bag, 1 clear beige bag
dim coral bag contain 2 shiny gray bag, 5 clear indigo bag, 2 vibrant plum bag
pale orange bag contain 2 plaid tomato bag
mirrored bronze bag contain 4 striped gray bag, 1 posh lavender bag, 2 wavy turquoise bag
dim magenta bag contain 5 vibrant maroon bag, 5 mirrored fuchsia bag, 5 pale bronze bag, 2 dim brown bag
plaid aqua bag contain 3 mirrored green bag
mirrored indigo bag contain 2 vibrant lime bag, 2 clear salmon bag, 4 wavy magenta bag
pale violet bag contain 1 clear salmon bag, 5 posh maroon bag, 4 posh plum bag
bright white bag contain 1 muted blue bag, 2 wavy chartreuse bag, 2 pale turquoise bag, 5 plaid red bag
faded lavender bag contain 2 light gold bag
pale salmon bag contain 3 pale turquoise bag, 2 faded black bag, 5 wavy green bag
vibrant teal bag contain 5 vibrant red bag, 1 dark silver bag, 2 pale white bag
dark teal bag contain 4 dim plum bag, 4 mirrored white bag, 1 wavy gold bag
dotted violet bag contain 1 clear beige bag
vibrant black bag contain 5 dim violet bag
bright gray bag contain 1 dull gray bag, 1 dark plum bag, 4 bright silver bag, 4 pale chartreuse bag
light black bag contain 1 faded chartreuse bag
muted coral bag contain 2 striped gray bag, 3 clear beige bag
dark orange bag contain 3 mirrored teal bag, 5 dotted blue bag, 1 vibrant lime bag
muted yellow bag contain 2 dim aqua bag, 4 vibrant indigo bag
posh chartreuse bag contain 5 light blue bag, 4 faded chartreuse bag, 4 shiny black bag, 1 dim violet bag
wavy maroon bag contain 5 muted gold bag, 4 posh yellow bag
dim orange bag contain 1 faded gold bag
dim aqua bag contain 4 wavy purple bag
faded turquoise bag contain 5 bright violet bag, 3 pale purple bag, 4 faded maroon bag
posh bronze bag contain 2 dim orange bag, 1 posh lavender bag
vibrant white bag contain 5 muted aqua bag, 5 shiny turquoise bag
clear blue bag contain 1 mirrored lavender bag, 2 dull violet bag
striped teal bag contain 2 vibrant cyan bag
striped tomato bag contain 1 dotted violet bag, 3 vibrant violet bag, 1 light beige bag
muted maroon bag contain 2 clear red bag, 2 plaid chartreuse bag, 2 posh tomato bag
dark bronze bag contain 5 dull white bag, 3 clear violet bag, 4 dark olive bag, 4 pale violet bag
light blue bag contain 1 muted violet bag, 4 dark gold bag, 3 pale blue bag
plaid white bag contain 3 striped orange bag, 3 light coral bag, 5 drab aqua bag
vibrant cyan bag contain 4 dim fuchsia bag, 5 dull blue bag
faded tomato bag contain 5 dim violet bag, 4 bright green bag, 3 bright teal bag
wavy fuchsia bag contain 5 striped coral bag, 3 dark maroon bag, 5 muted aqua bag
drab brown bag contain 5 wavy orange bag, 4 clear violet bag
shiny olive bag contain 5 pale red bag, 1 bright purple bag, 2 dark plum bag
mirrored fuchsia bag contain 4 dark violet bag, 2 faded crimson bag, 4 striped black bag
clear olive bag contain 2 wavy magenta bag, 1 striped black bag, 5 pale fuchsia bag, 4 drab red bag
dim yellow bag contain 2 faded blue bag, 2 shiny lavender bag, 5 shiny silver bag
dark silver bag contain 4 light aqua bag
plaid tomato bag contain 2 posh aqua bag, 2 striped turquoise bag, 3 plaid plum bag
clear magenta bag contain 2 muted violet bag
dotted orange bag contain 3 striped turquoise bag
striped fuchsia bag contain 4 clear beige bag, 4 shiny crimson bag, 1 striped red bag, 4 shiny lavender bag
clear gray bag contain 5 vibrant aqua bag, 1 light teal bag, 2 striped lime bag, 3 vibrant cyan bag
dotted gold bag contain 4 drab gold bag, 2 faded tomato bag, 1 pale gray bag
clear orange bag contain 3 mirrored plum bag, 1 dim aqua bag, 1 drab bronze bag
vibrant blue bag contain 1 shiny brown bag, 5 shiny crimson bag
pale plum bag contain 3 wavy olive bag, 5 pale lime bag, 3 plaid gold bag, 1 dim gold bag
dim lavender bag contain 5 striped black bag, 2 vibrant lime bag, 4 bright red bag
dull purple bag contain 1 dark tomato bag, 5 faded crimson bag
vibrant tan bag contain 4 dim tomato bag, 4 vibrant violet bag, 5 pale olive bag, 2 posh aqua bag
dull magenta bag contain 4 bright gray bag, 5 faded gold bag, 3 dotted yellow bag, 3 bright silver bag
posh violet bag contain 5 vibrant indigo bag, 5 pale chartreuse bag, 2 dark green bag, 3 light blue bag
dotted green bag contain 4 clear red bag, 5 drab aqua bag, 3 light black bag
pale magenta bag contain 5 dark maroon bag, 3 mirrored aqua bag
pale indigo bag contain 3 drab turquoise bag, 5 light violet bag, 5 clear magenta bag, 1 striped blue bag
dotted lime bag contain 4 dull tomato bag, 5 dull yellow bag, 4 shiny gold bag
posh fuchsia bag contain 2 pale orange bag, 4 posh coral bag, 1 drab brown bag
light teal bag contain 3 faded green bag
shiny lime bag contain 4 dotted blue bag, 5 light coral bag
dull blue bag contain 0 other bag
pale turquoise bag contain 2 pale blue bag, 5 dotted purple bag
striped gold bag contain 2 wavy silver bag, 3 light purple bag, 3 dull gold bag, 1 dark coral bag
vibrant chartreuse bag contain 5 mirrored tan bag, 4 vibrant blue bag, 1 clear teal bag, 2 dull indigo bag
muted silver bag contain 1 dark beige bag
shiny red bag contain 3 dim fuchsia bag, 3 wavy gold bag, 3 posh violet bag, 3 shiny silver bag
mirrored chartreuse bag contain 1 wavy white bag
light red bag contain 4 mirrored gold bag
pale chartreuse bag contain 1 pale lime bag, 4 dim cyan bag
bright aqua bag contain 5 bright yellow bag, 1 drab orange bag
wavy lavender bag contain 5 dark white bag, 3 muted blue bag, 1 dotted salmon bag, 2 dull silver bag
dotted purple bag contain 5 light aqua bag
drab red bag contain 4 wavy green bag
dull indigo bag contain 2 dark teal bag, 5 drab turquoise bag
striped lime bag contain 3 dull blue bag, 2 shiny lavender bag, 2 muted aqua bag, 3 posh silver bag
clear red bag contain 3 shiny fuchsia bag
mirrored plum bag contain 1 muted fuchsia bag
light chartreuse bag contain 3 mirrored salmon bag, 3 clear indigo bag, 1 striped coral bag, 1 plaid blue bag
striped plum bag contain 3 pale violet bag
light gold bag contain 2 dim fuchsia bag
shiny white bag contain 5 dark indigo bag, 2 dim aqua bag, 5 vibrant aqua bag
faded bronze bag contain 5 dim cyan bag
pale red bag contain 2 mirrored magenta bag, 1 bright cyan bag, 2 vibrant lime bag
muted chartreuse bag contain 2 bright chartreuse bag, 1 wavy gray bag, 1 pale lime bag, 5 light teal bag
wavy chartreuse bag contain 4 bright fuchsia bag, 3 vibrant violet bag, 2 dull aqua bag
dull lime bag contain 5 shiny lavender bag, 3 posh aqua bag
vibrant magenta bag contain 5 striped yellow bag, 2 light tan bag, 5 shiny brown bag, 2 muted yellow bag
muted blue bag contain 3 vibrant aqua bag, 2 dim fuchsia bag
drab aqua bag contain 1 plaid plum bag, 1 posh yellow bag, 1 muted fuchsia bag, 4 muted indigo bag
mirrored beige bag contain 5 wavy brown bag, 2 clear crimson bag, 2 dim gold bag
light tan bag contain 5 light violet bag, 5 dim brown bag, 5 wavy turquoise bag
faded fuchsia bag contain 5 drab brown bag, 2 light aqua bag
dim salmon bag contain 4 shiny cyan bag, 4 faded olive bag, 3 dark maroon bag
drab lavender bag contain 2 drab gray bag, 5 clear black bag, 1 shiny plum bag
mirrored white bag contain 3 plaid plum bag, 5 muted coral bag, 1 clear gold bag
dull aqua bag contain 3 shiny lavender bag, 1 muted aqua bag, 4 light purple bag, 4 shiny brown bag
plaid maroon bag contain 4 clear lime bag, 1 muted violet bag, 4 vibrant teal bag
clear salmon bag contain 2 striped blue bag, 1 dim chartreuse bag, 3 light purple bag, 2 posh silver bag
dotted lavender bag contain 1 dark tomato bag, 2 striped turquoise bag, 3 dull gray bag
light green bag contain 4 bright silver bag, 1 dim plum bag, 5 dark indigo bag, 5 dark blue bag
plaid black bag contain 4 muted lavender bag, 5 muted violet bag, 3 dim olive bag, 5 bright maroon bag
dull brown bag contain 3 dull green bag
dull fuchsia bag contain 2 dotted blue bag, 4 vibrant bronze bag, 5 striped red bag
light olive bag contain 3 clear beige bag, 3 bright maroon bag, 1 dim green bag
faded beige bag contain 2 striped black bag, 5 light coral bag
light coral bag contain 3 clear gold bag, 2 drab magenta bag, 2 pale lime bag
shiny turquoise bag contain 4 dull olive bag, 1 pale purple bag, 5 striped bronze bag
dark chartreuse bag contain 3 dotted beige bag, 1 dull silver bag, 3 posh lavender bag, 5 dotted blue bag
shiny brown bag contain 5 plaid plum bag, 3 vibrant lime bag, 1 posh silver bag, 5 muted aqua bag
dim gold bag contain 4 wavy magenta bag, 1 plaid turquoise bag, 3 drab maroon bag, 3 dark coral bag
faded teal bag contain 2 dim turquoise bag, 4 faded beige bag
dull lavender bag contain 3 shiny chartreuse bag, 4 posh salmon bag
mirrored brown bag contain 4 vibrant cyan bag
striped black bag contain 2 dull blue bag, 1 vibrant aqua bag, 1 dark maroon bag
mirrored violet bag contain 3 vibrant crimson bag, 1 posh violet bag
dark beige bag contain 3 mirrored gold bag
clear white bag contain 2 striped gray bag
dull tan bag contain 3 mirrored red bag, 2 plaid indigo bag, 3 bright gray bag
dim tomato bag contain 1 faded beige bag, 2 dotted beige bag
dark black bag contain 2 clear silver bag
shiny magenta bag contain 5 plaid blue bag, 5 shiny aqua bag, 1 dull aqua bag
light plum bag contain 1 dim black bag, 3 faded olive bag
shiny beige bag contain 5 vibrant plum bag, 5 light blue bag, 2 light salmon bag, 3 wavy tan bag
wavy gold bag contain 1 drab aqua bag
vibrant lime bag contain 0 other bag
vibrant turquoise bag contain 1 vibrant blue bag, 4 striped teal bag, 5 striped white bag
dim maroon bag contain 4 striped lime bag, 2 light orange bag, 2 vibrant maroon bag
posh olive bag contain 5 plaid tomato bag, 4 dark magenta bag, 4 faded chartreuse bag
dim white bag contain 3 striped blue bag
faded purple bag contain 1 dim brown bag, 3 dark orange bag, 2 posh silver bag, 5 muted lavender bag
faded brown bag contain 5 faded coral bag, 1 striped turquoise bag
posh beige bag contain 4 pale lime bag, 4 light violet bag
shiny gray bag contain 2 shiny black bag, 5 striped white bag
dotted salmon bag contain 3 pale lime bag, 3 muted lavender bag, 3 vibrant red bag
vibrant brown bag contain 5 light gold bag, 3 light purple bag, 4 light blue bag
faded white bag contain 1 dotted black bag
wavy turquoise bag contain 4 dim crimson bag, 3 bright maroon bag, 3 pale cyan bag
drab cyan bag contain 4 drab olive bag, 3 dim tomato bag, 2 muted indigo bag
drab indigo bag contain 5 shiny bronze bag, 4 striped crimson bag, 5 light gold bag
dim red bag contain 2 dull aqua bag, 3 mirrored aqua bag, 1 wavy red bag, 2 shiny crimson bag
wavy coral bag contain 3 bright tan bag, 1 bright coral bag, 4 dull gold bag
pale tan bag contain 2 clear blue bag, 3 dark bronze bag, 2 plaid coral bag, 3 vibrant magenta bag
wavy lime bag contain 4 dull silver bag
muted indigo bag contain 5 light purple bag
clear bronze bag contain 4 clear silver bag, 3 shiny tan bag
dull maroon bag contain 4 dark blue bag, 4 mirrored indigo bag
clear yellow bag contain 3 plaid coral bag, 3 drab lime bag, 3 faded indigo bag
drab green bag contain 5 faded purple bag
plaid olive bag contain 5 faded silver bag, 4 dull purple bag, 4 dull yellow bag, 1 plaid salmon bag
dark brown bag contain 1 clear gold bag, 5 light coral bag
wavy tomato bag contain 4 striped teal bag
dotted maroon bag contain 1 posh silver bag, 1 dark turquoise bag
posh plum bag contain 2 bright red bag, 3 shiny maroon bag
faded violet bag contain 1 faded green bag
bright tan bag contain 3 shiny blue bag, 1 mirrored lime bag, 2 vibrant plum bag
dim beige bag contain 1 light tan bag, 1 pale silver bag, 5 plaid silver bag
clear plum bag contain 1 dark silver bag, 4 dull green bag, 3 shiny gray bag
muted lavender bag contain 5 dim olive bag, 1 pale lime bag
faded gold bag contain 1 striped coral bag, 3 light aqua bag
faded orange bag contain 4 faded beige bag
dim fuchsia bag contain 0 other bag
dull green bag contain 5 dull purple bag, 3 bright maroon bag, 1 dark plum bag
muted turquoise bag contain 5 shiny chartreuse bag, 1 mirrored lime bag
striped cyan bag contain 3 striped gray bag, 4 dark brown bag
faded cyan bag contain 4 striped purple bag
shiny maroon bag contain 5 faded silver bag, 5 dark purple bag, 5 pale gold bag
wavy tan bag contain 3 dim brown bag
clear silver bag contain 5 clear blue bag, 1 dim chartreuse bag, 2 clear orange bag
dull gold bag contain 3 drab aqua bag, 1 dim green bag
wavy gray bag contain 2 striped bronze bag
shiny purple bag contain 3 wavy lavender bag, 2 striped yellow bag
posh salmon bag contain 1 dull black bag, 3 muted aqua bag, 4 muted fuchsia bag, 5 bright coral bag
faded gray bag contain 2 faded orange bag, 1 striped brown bag
shiny indigo bag contain 5 posh beige bag
vibrant gray bag contain 3 pale brown bag, 2 shiny tomato bag, 5 mirrored silver bag, 3 striped tomato bag
posh gray bag contain 4 striped black bag, 3 muted aqua bag, 4 mirrored gold bag
mirrored cyan bag contain 1 muted lavender bag, 4 striped lime bag, 3 mirrored blue bag
dull yellow bag contain 5 shiny brown bag, 5 clear maroon bag, 4 dim cyan bag
mirrored black bag contain 2 mirrored aqua bag
dim purple bag contain 4 vibrant teal bag, 5 shiny silver bag, 3 shiny brown bag
drab beige bag contain 1 dim yellow bag, 1 vibrant lime bag, 2 muted plum bag, 5 posh violet bag
striped chartreuse bag contain 2 posh gold bag, 1 striped lime bag
dull chartreuse bag contain 1 plaid plum bag
bright red bag contain 2 light lavender bag, 1 drab magenta bag
drab crimson bag contain 2 pale chartreuse bag, 1 muted black bag, 4 striped yellow bag, 4 striped black bag
wavy aqua bag contain 4 light tan bag, 3 dim maroon bag, 1 bright fuchsia bag
clear gold bag contain 0 other bag
dim lime bag contain 1 dull crimson bag, 1 mirrored orange bag, 1 light yellow bag, 1 muted fuchsia bag
pale cyan bag contain 5 dull blue bag, 5 dark blue bag
dim silver bag contain 3 bright aqua bag
dark maroon bag contain 4 striped turquoise bag, 4 faded green bag, 3 dim fuchsia bag
striped tan bag contain 2 dark violet bag, 2 muted indigo bag
posh tomato bag contain 3 dark purple bag, 3 dim olive bag, 2 dotted white bag, 3 mirrored cyan bag
light silver bag contain 1 plaid orange bag, 3 wavy salmon bag
muted brown bag contain 1 plaid orange bag
dim indigo bag contain 2 dark teal bag, 5 faded beige bag, 1 drab gray bag, 4 muted gold bag
wavy brown bag contain 3 dotted salmon bag
posh purple bag contain 2 wavy salmon bag, 1 faded tomato bag, 5 dark tan bag
muted fuchsia bag contain 3 muted violet bag, 5 light purple bag, 4 dim green bag
muted lime bag contain 2 vibrant beige bag
muted black bag contain 5 pale blue bag, 1 vibrant beige bag, 4 pale lime bag, 2 vibrant cyan bag
drab white bag contain 2 dim magenta bag, 5 vibrant bronze bag, 3 bright magenta bag
bright chartreuse bag contain 5 dark white bag, 3 dotted olive bag
wavy yellow bag contain 2 dotted salmon bag
posh green bag contain 5 posh magenta bag, 2 light aqua bag, 3 wavy purple bag
clear violet bag contain 3 mirrored salmon bag
dull plum bag contain 4 bright coral bag
posh yellow bag contain 4 dim aqua bag, 1 shiny brown bag, 3 striped orange bag
dark salmon bag contain 4 light gold bag, 3 dotted white bag, 5 drab gray bag, 4 vibrant cyan bag
posh blue bag contain 4 vibrant salmon bag, 2 clear tan bag, 5 light tomato bag, 1 wavy maroon bag
drab bronze bag contain 5 plaid green bag, 4 striped turquoise bag, 2 shiny aqua bag, 3 bright plum bag
dotted aqua bag contain 3 wavy olive bag
dark lavender bag contain 2 dotted plum bag
shiny tan bag contain 4 dotted turquoise bag, 4 pale violet bag, 3 plaid salmon bag, 1 striped gold bag
shiny orange bag contain 3 dull purple bag, 1 clear green bag
muted olive bag contain 2 dark orange bag
dark tomato bag contain 5 vibrant lime bag
vibrant silver bag contain 4 striped blue bag, 2 plaid gold bag
dull bronze bag contain 3 faded coral bag, 1 clear chartreuse bag, 2 muted aqua bag, 3 wavy teal bag
light tomato bag contain 3 dark blue bag, 5 mirrored salmon bag
dotted cyan bag contain 2 dark gold bag, 4 clear gray bag, 2 dull aqua bag
bright purple bag contain 4 striped coral bag
dark white bag contain 3 dim brown bag, 1 mirrored gold bag, 1 striped white bag, 4 plaid black bag
light magenta bag contain 4 vibrant olive bag, 5 clear lavender bag, 5 faded yellow bag
drab violet bag contain 3 dotted blue bag, 2 dark plum bag, 3 dim silver bag, 5 vibrant olive bag
posh turquoise bag contain 2 muted indigo bag, 2 striped white bag, 3 drab bronze bag, 4 dotted black bag
plaid tan bag contain 3 vibrant bronze bag, 5 dull purple bag, 2 posh turquoise bag
dull violet bag contain 4 vibrant cyan bag
drab gray bag contain 3 pale lime bag, 3 bright green bag, 3 light lavender bag, 5 dull gray bag
faded blue bag contain 5 muted lavender bag, 2 dim fuchsia bag, 3 clear salmon bag, 4 striped blue bag
mirrored turquoise bag contain 5 faded purple bag
wavy bronze bag contain 3 dim green bag, 2 muted indigo bag, 5 dotted tan bag
light brown bag contain 3 bright purple bag, 4 vibrant lime bag
bright brown bag contain 4 light coral bag, 3 clear gold bag, 2 striped turquoise bag, 4 dim fuchsia bag
dotted turquoise bag contain 1 striped white bag, 4 dark magenta bag
wavy teal bag contain 5 shiny lime bag, 2 dull cyan bag
dark gold bag contain 5 dim green bag, 2 plaid red bag, 2 pale chartreuse bag
dotted black bag contain 3 drab olive bag, 3 light teal bag
wavy blue bag contain 4 clear red bag
posh red bag contain 3 muted tan bag
shiny black bag contain 5 light maroon bag, 4 vibrant cyan bag, 2 mirrored indigo bag
plaid fuchsia bag contain 3 wavy magenta bag, 4 posh aqua bag, 3 posh salmon bag
dotted olive bag contain 5 bright brown bag, 1 dotted salmon bag, 4 striped turquoise bag
dull teal bag contain 2 pale purple bag
posh indigo bag contain 1 shiny salmon bag
clear coral bag contain 2 muted violet bag
pale silver bag contain 2 drab olive bag, 5 wavy red bag
light beige bag contain 2 muted lime bag
striped orange bag contain 0 other bag
dark gray bag contain 4 pale white bag, 3 pale blue bag, 5 dotted beige bag
striped lavender bag contain 2 dull brown bag, 4 vibrant lavender bag, 1 vibrant aqua bag, 5 dull gold bag
dark blue bag contain 5 clear gold bag, 5 faded silver bag
plaid orange bag contain 1 shiny tomato bag, 1 light tomato bag
muted bronze bag contain 2 clear gray bag, 5 shiny black bag, 5 shiny red bag, 2 muted blue bag
light cyan bag contain 4 wavy crimson bag, 4 muted bronze bag, 4 clear lime bag, 3 dull yellow bag
light salmon bag contain 4 muted aqua bag, 5 vibrant lime bag, 4 light aqua bag, 4 dim fuchsia bag
dotted fuchsia bag contain 1 mirrored aqua bag
drab tomato bag contain 2 vibrant blue bag, 1 pale chartreuse bag, 4 shiny black bag, 5 drab silver bag
drab black bag contain 3 mirrored teal bag, 5 dull maroon bag
posh black bag contain 4 pale violet bag, 5 plaid violet bag, 2 posh magenta bag
vibrant aqua bag contain 1 faded silver bag
mirrored tan bag contain 3 dotted white bag
mirrored teal bag contain 3 shiny plum bag, 3 shiny brown bag, 3 striped turquoise bag, 2 bright red bag
muted white bag contain 5 drab gray bag, 5 faded white bag, 3 vibrant beige bag
bright beige bag contain 3 vibrant red bag, 4 posh silver bag
dark indigo bag contain 2 dark violet bag, 2 dim plum bag, 1 mirrored indigo bag
striped maroon bag contain 5 faded blue bag
clear chartreuse bag contain 5 plaid plum bag, 1 plaid maroon bag, 1 dark crimson bag, 4 drab bronze bag
dark olive bag contain 2 wavy purple bag, 4 shiny lime bag
dim olive bag contain 5 faded silver bag, 5 shiny plum bag
light indigo bag contain 5 dotted tomato bag, 1 dim orange bag, 3 mirrored orange bag, 3 pale cyan bag
faded yellow bag contain 4 light red bag, 5 clear black bag, 2 dotted gold bag
clear teal bag contain 2 light maroon bag
drab lime bag contain 4 dim blue bag, 3 muted gold bag, 3 faded crimson bag
dotted chartreuse bag contain 1 vibrant chartreuse bag, 3 posh red bag, 5 muted bronze bag, 4 dark brown bag
drab olive bag contain 1 striped orange bag, 3 drab brown bag
posh gold bag contain 3 plaid beige bag, 4 dim crimson bag, 2 dull black bag
wavy indigo bag contain 3 bright brown bag, 3 pale cyan bag, 4 mirrored orange bag, 1 clear cyan bag
bright black bag contain 1 muted crimson bag
pale fuchsia bag contain 5 dull yellow bag, 4 bright chartreuse bag
shiny coral bag contain 1 muted lavender bag, 5 muted purple bag, 1 striped orange bag
faded chartreuse bag contain 4 striped turquoise bag, 1 wavy beige bag
bright blue bag contain 3 vibrant olive bag
faded olive bag contain 3 vibrant maroon bag, 4 wavy red bag, 2 shiny cyan bag, 4 wavy salmon bag
clear green bag contain 5 dark turquoise bag, 4 posh cyan bag, 5 pale orange bag
dim bronze bag contain 4 wavy orange bag, 2 bright magenta bag, 3 striped brown bag
pale gold bag contain 3 dark purple bag
wavy beige bag contain 2 wavy plum bag, 1 muted purple bag, 4 striped turquoise bag, 4 dull green bag
plaid lavender bag contain 3 striped plum bag, 3 plaid orange bag
bright silver bag contain 2 muted aqua bag
muted magenta bag contain 5 faded olive bag
drab magenta bag contain 4 dim chartreuse bag
pale yellow bag contain 2 wavy tan bag, 4 striped cyan bag, 1 wavy salmon bag
clear tomato bag contain 1 clear blue bag, 5 vibrant orange bag, 3 drab silver bag, 2 dim green bag
dull gray bag contain 2 bright red bag, 3 striped lime bag
dim gray bag contain 4 dark purple bag, 2 dim tomato bag
mirrored crimson bag contain 4 pale gray bag, 1 muted chartreuse bag, 2 dotted orange bag
drab gold bag contain 4 drab lavender bag, 3 light coral bag
posh tan bag contain 5 vibrant gold bag, 1 dotted purple bag
drab teal bag contain 3 shiny gold bag, 2 muted blue bag, 2 posh coral bag, 3 bright lavender bag
pale olive bag contain 2 dull violet bag, 5 shiny maroon bag, 4 light red bag, 2 wavy cyan bag
dotted coral bag contain 1 light blue bag, 2 plaid black bag
light aqua bag contain 1 vibrant lime bag, 3 clear gold bag, 1 plaid plum bag, 5 shiny plum bag
posh magenta bag contain 4 plaid plum bag, 2 vibrant lime bag, 5 light aqua bag, 2 dull blue bag
posh coral bag contain 3 dotted salmon bag, 2 dim lavender bag, 4 wavy purple bag
dark plum bag contain 2 vibrant aqua bag, 2 dim fuchsia bag, 4 dull blue bag
posh teal bag contain 4 mirrored indigo bag, 3 striped purple bag, 5 dim cyan bag, 4 plaid silver bag
vibrant salmon bag contain 3 faded lime bag
vibrant violet bag contain 5 bright red bag, 3 shiny brown bag, 3 vibrant cyan bag
plaid violet bag contain 2 vibrant violet bag, 4 pale brown bag
dull red bag contain 1 dim aqua bag, 5 dotted magenta bag, 1 dotted gold bag, 2 shiny chartreuse bag
vibrant coral bag contain 2 bright green bag
muted cyan bag contain 4 dull white bag, 3 muted gray bag, 1 mirrored brown bag, 5 light maroon bag
dotted tan bag contain 4 shiny indigo bag, 3 clear gold bag
muted tomato bag contain 1 faded orange bag
clear black bag contain 2 light aqua bag, 5 dull white bag
bright fuchsia bag contain 5 dim brown bag
striped olive bag contain 4 dim tomato bag
dotted yellow bag contain 4 mirrored aqua bag, 4 faded indigo bag, 2 faded green bag
pale bronze bag contain 3 plaid teal bag, 2 posh aqua bag, 2 dotted lime bag
striped blue bag contain 4 dark tomato bag, 2 dim aqua bag, 1 dull olive bag
dull salmon bag contain 1 light yellow bag
muted tan bag contain 2 dim purple bag, 2 shiny coral bag, 2 drab bronze bag
bright gold bag contain 5 shiny lavender bag, 4 dark maroon bag
vibrant lavender bag contain 3 vibrant lime bag, 1 dark tomato bag, 2 dim fuchsia bag, 4 clear black bag
bright tomato bag contain 4 clear blue bag, 2 wavy beige bag, 5 faded lime bag
drab plum bag contain 4 bright olive bag, 1 posh lavender bag, 3 pale white bag, 2 dim green bag
muted gold bag contain 3 posh magenta bag
mirrored coral bag contain 3 dotted beige bag, 1 light magenta bag, 4 wavy turquoise bag
mirrored purple bag contain 1 mirrored plum bag, 4 faded black bag, 3 bright violet bag, 1 vibrant yellow bag
mirrored lavender bag contain 4 shiny violet bag, 4 dark violet bag, 3 drab gray bag, 3 plaid salmon bag
muted teal bag contain 1 plaid turquoise bag, 5 light tomato bag
plaid turquoise bag contain 2 posh aqua bag, 3 wavy plum bag, 3 dotted salmon bag
pale coral bag contain 4 wavy lavender bag, 5 striped gray bag, 2 dotted turquoise bag, 4 striped violet bag
pale lavender bag contain 4 vibrant lime bag, 1 dim plum bag, 1 posh salmon bag
dark lime bag contain 4 dotted beige bag, 4 faded gold bag
dotted teal bag contain 3 posh cyan bag
striped magenta bag contain 4 light maroon bag
light lime bag contain 2 light tomato bag, 2 bright cyan bag, 1 dotted white bag, 5 dark turquoise bag
plaid teal bag contain 4 dim cyan bag, 2 muted black bag, 1 dark silver bag, 4 drab lavender bag
vibrant yellow bag contain 4 mirrored teal bag, 2 shiny lime bag, 1 striped purple bag, 2 dotted beige bag
dotted plum bag contain 1 drab lavender bag
dotted blue bag contain 4 dull white bag, 5 dull olive bag
posh crimson bag contain 1 wavy plum bag, 4 dim bronze bag
muted orange bag contain 5 faded tomato bag, 1 dull magenta bag
mirrored gold bag contain 4 dim fuchsia bag, 3 dull black bag, 5 shiny lavender bag, 5 dull gray bag
bright cyan bag contain 4 pale blue bag
dark cyan bag contain 2 dim olive bag, 2 faded crimson bag, 2 pale chartreuse bag
striped beige bag contain 5 drab lavender bag
dull olive bag contain 4 dark brown bag, 5 muted lavender bag, 4 plaid red bag, 1 dim green bag
faded green bag contain 5 light aqua bag, 1 vibrant cyan bag, 5 striped orange bag
shiny bronze bag contain 1 shiny purple bag, 5 striped indigo bag, 5 bright indigo bag, 5 striped yellow bag
mirrored silver bag contain 2 pale tan bag
dark green bag contain 4 striped white bag, 2 vibrant beige bag, 4 shiny aqua bag, 2 drab gray bag
dotted gray bag contain 3 dotted violet bag, 5 muted beige bag, 4 posh yellow bag
clear lime bag contain 5 faded crimson bag, 5 dark brown bag, 1 dim chartreuse bag, 5 bright fuchsia bag
light maroon bag contain 5 light aqua bag
striped violet bag contain 2 clear violet bag, 1 striped yellow bag, 5 dark lime bag
mirrored maroon bag contain 2 dull purple bag, 3 clear black bag
light purple bag contain 1 vibrant aqua bag, 4 striped turquoise bag, 4 dark blue bag, 3 dark maroon bag
dark crimson bag contain 5 dark blue bag, 1 dim coral bag
muted violet bag contain 3 striped turquoise bag, 3 vibrant lime bag
shiny tomato bag contain 4 shiny plum bag
drab fuchsia bag contain 2 faded beige bag, 3 light lavender bag
dull white bag contain 5 wavy purple bag, 4 shiny lavender bag
dim plum bag contain 4 dark brown bag, 3 shiny brown bag, 4 dim brown bag, 5 light maroon bag
muted red bag contain 3 bright chartreuse bag, 2 shiny lime bag, 1 dotted olive bag, 3 shiny plum bag
posh silver bag contain 0 other bag
drab coral bag contain 4 faded white bag, 5 mirrored plum bag, 5 striped blue bag
mirrored aqua bag contain 1 dark tomato bag, 2 dark brown bag
vibrant indigo bag contain 5 dark silver bag, 3 clear lime bag, 1 dim gray bag
bright salmon bag contain 4 bright crimson bag
muted plum bag contain 4 mirrored lavender bag
dark turquoise bag contain 5 striped turquoise bag, 4 dark blue bag, 5 posh yellow bag, 4 wavy purple bag
light violet bag contain 3 clear black bag, 3 mirrored indigo bag, 5 striped coral bag, 2 dim crimson bag
'''

TEST = '''light red bag contain 1 bright white bag, 2 muted yellow bag
dark orange bag contain 3 bright white bag, 4 muted yellow bag
bright white bag contain 1 shiny gold bag
muted yellow bag contain 2 shiny gold bag, 9 faded blue bag
shiny gold bag contain 1 dark olive bag, 2 vibrant plum bag
dark olive bag contain 3 faded blue bag, 4 dotted black bag
vibrant plum bag contain 5 faded blue bag, 6 dotted black bag
faded blue bag contain 0 other bag
dotted black bag contain 0 other bag
'''

def solve(cases):
    map = make_map(cases)
    
    count = 0
    for key in map:
        to_find = []
        found = 0
        for item in map[key]:
            new_key = item[0]
            to_find.append(new_key)
        # print('initial', to_find)
        searched = set()
        while len(to_find) > 0:
            new_key = to_find[0]
            to_find = to_find[1:]
            if new_key == 'shiny gold':
                # print('found under', key)
                found = 1
                break
            if new_key not in map:
                # print('could not find', new_key)
                continue
            for item in map[new_key]:
                new_key = item[0]
                if new_key == 'shiny gold':
                    # print('found under', key)
                    found = 1
                    break
                if new_key in searched:
                    continue
                searched.add(item[0])
                to_find.append(item[0])
            if found:
                break
        count += found
    return count

def make_map(cases):
    cases = cases.split('\n')

    map = {}

    for i in range(len(cases)):
        if not cases[i] or type(cases[i]) == type([]):
            continue

        case = cases[i].split(',')
        new_case = []
        for j in range(len(case)):
            new_case += case[j].split('contain')
        case = []
        for k in range(len(new_case)):
            case.append(new_case[k].split(' bag')[0])

        result = []
        for l in range(len(case)):
            if l == 0:
                result.append(case[l])
            else:
                case[l] = case[l].strip()
                words = case[l].split(' ')
                color = ' '.join(words[1:])
                count = int(words[0])
                color.strip()
                result.append((color, count))
        map[result[0]] = result[1:]
    return map


def contained_by(map, color):
    inside = map[color]
    included = 1
    for bag in inside:
        if bag[0] == 'other':
            continue
        print(bag)
        included += bag[1] * max(1 ,contained_by(map, bag[0]))
    print(included)
    return included

if __name__ == '__main__':
    test_results = solve(TEST)
    if test_results != 4:
        print(test_results, 'should be 4')
        exit()
    print('results', test_results)

    results = solve(INPUT)
    print(results)


    map = make_map(INPUT)
    included = 0
    inside = map['shiny gold']
    print(inside)
    for bag in inside:
        included += bag[1] * contained_by(map, bag[0])
    print(included)
