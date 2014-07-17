#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2011 thomasv@gitorious
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.



# list of words from http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Contemporary_poetry

words_en = [
"like",
"just",
"love",
"know",
"never",
"want",
"time",
"out",
"there",
"make",
"look",
"eye",
"down",
"only",
"think",
"heart",
"back",
"then",
"into",
"about",
"more",
"away",
"still",
"them",
"take",
"thing",
"even",
"through",
"long",
"always",
"world",
"too",
"friend",
"tell",
"try",
"hand",
"thought",
"over",
"here",
"other",
"need",
"smile",
"again",
"much",
"cry",
"been",
"night",
"ever",
"little",
"said",
"end",
"some",
"those",
"around",
"mind",
"people",
"girl",
"leave",
"dream",
"left",
"turn",
"myself",
"give",
"nothing",
"really",
"off",
"before",
"something",
"find",
"walk",
"wish",
"good",
"once",
"place",
"ask",
"stop",
"keep",
"watch",
"seem",
"everything",
"wait",
"got",
"yet",
"made",
"remember",
"start",
"alone",
"run",
"hope",
"maybe",
"believe",
"body",
"hate",
"after",
"close",
"talk",
"stand",
"own",
"each",
"hurt",
"help",
"home",
"god",
"soul",
"new",
"many",
"two",
"inside",
"should",
"true",
"first",
"fear",
"mean",
"better",
"play",
"another",
"gone",
"change",
"use",
"wonder",
"someone",
"hair",
"cold",
"open",
"best",
"any",
"behind",
"happen",
"water",
"dark",
"laugh",
"stay",
"forever",
"name",
"work",
"show",
"sky",
"break",
"came",
"deep",
"door",
"put",
"black",
"together",
"upon",
"happy",
"such",
"great",
"white",
"matter",
"fill",
"past",
"please",
"burn",
"cause",
"enough",
"touch",
"moment",
"soon",
"voice",
"scream",
"anything",
"stare",
"sound",
"red",
"everyone",
"hide",
"kiss",
"truth",
"death",
"beautiful",
"mine",
"blood",
"broken",
"very",
"pass",
"next",
"forget",
"tree",
"wrong",
"air",
"mother",
"understand",
"lip",
"hit",
"wall",
"memory",
"sleep",
"free",
"high",
"realize",
"school",
"might",
"skin",
"sweet",
"perfect",
"blue",
"kill",
"breath",
"dance",
"against",
"fly",
"between",
"grow",
"strong",
"under",
"listen",
"bring",
"sometimes",
"speak",
"pull",
"person",
"become",
"family",
"begin",
"ground",
"real",
"small",
"father",
"sure",
"feet",
"rest",
"young",
"finally",
"land",
"across",
"today",
"different",
"guy",
"line",
"fire",
"reason",
"reach",
"second",
"slowly",
"write",
"eat",
"smell",
"mouth",
"step",
"learn",
"three",
"floor",
"promise",
"breathe",
"darkness",
"push",
"earth",
"guess",
"save",
"song",
"above",
"along",
"both",
"color",
"house",
"almost",
"sorry",
"anymore",
"brother",
"okay",
"dear",
"game",
"fade",
"already",
"apart",
"warm",
"beauty",
"heard",
"notice",
"question",
"shine",
"began",
"piece",
"whole",
"shadow",
"secret",
"street",
"within",
"finger",
"point",
"morning",
"whisper",
"child",
"moon",
"green",
"story",
"glass",
"kid",
"silence",
"since",
"soft",
"yourself",
"empty",
"shall",
"angel",
"answer",
"baby",
"bright",
"dad",
"path",
"worry",
"hour",
"drop",
"follow",
"power",
"war",
"half",
"flow",
"heaven",
"act",
"chance",
"fact",
"least",
"tired",
"children",
"near",
"quite",
"afraid",
"rise",
"sea",
"taste",
"window",
"cover",
"nice",
"trust",
"lot",
"sad",
"cool",
"force",
"peace",
"return",
"blind",
"easy",
"ready",
"roll",
"rose",
"drive",
"held",
"music",
"beneath",
"hang",
"mom",
"paint",
"emotion",
"quiet",
"clear",
"cloud",
"few",
"pretty",
"bird",
"outside",
"paper",
"picture",
"front",
"rock",
"simple",
"anyone",
"meant",
"reality",
"road",
"sense",
"waste",
"bit",
"leaf",
"thank",
"happiness",
"meet",
"men",
"smoke",
"truly",
"decide",
"self",
"age",
"book",
"form",
"alive",
"carry",
"escape",
"damn",
"instead",
"able",
"ice",
"minute",
"throw",
"catch",
"leg",
"ring",
"course",
"goodbye",
"lead",
"poem",
"sick",
"corner",
"desire",
"known",
"problem",
"remind",
"shoulder",
"suppose",
"toward",
"wave",
"drink",
"jump",
"woman",
"pretend",
"sister",
"week",
"human",
"joy",
"crack",
"grey",
"pray",
"surprise",
"dry",
"knee",
"less",
"search",
"bleed",
"caught",
"clean",
"embrace",
"future",
"king",
"son",
"sorrow",
"chest",
"hug",
"remain",
"sat",
"worth",
"blow",
"daddy",
"final",
"parent",
"tight",
"also",
"create",
"lonely",
"safe",
"cross",
"dress",
"evil",
"silent",
"bone",
"fate",
"perhaps",
"anger",
"class",
"scar",
"snow",
"tiny",
"tonight",
"continue",
"control",
"dog",
"edge",
"mirror",
"month",
"suddenly",
"comfort",
"given",
"loud",
"quickly",
"gaze",
"plan",
"rush",
"stone",
"town",
"battle",
"ignore",
"spirit",
"stood",
"stupid",
"yours",
"brown",
"build",
"dust",
"hey",
"kept",
"pay",
"phone",
"twist",
"although",
"ball",
"beyond",
"hidden",
"nose",
"taken",
"fail",
"float",
"pure",
"somehow",
"wash",
"wrap",
"angry",
"cheek",
"creature",
"forgotten",
"heat",
"rip",
"single",
"space",
"special",
"weak",
"whatever",
"yell",
"anyway",
"blame",
"job",
"choose",
"country",
"curse",
"drift",
"echo",
"figure",
"grew",
"laughter",
"neck",
"suffer",
"worse",
"yeah",
"disappear",
"foot",
"forward",
"knife",
"mess",
"somewhere",
"stomach",
"storm",
"beg",
"idea",
"lift",
"offer",
"breeze",
"field",
"five",
"often",
"simply",
"stuck",
"win",
"allow",
"confuse",
"enjoy",
"except",
"flower",
"seek",
"strength",
"calm",
"grin",
"gun",
"heavy",
"hill",
"large",
"ocean",
"shoe",
"sigh",
"straight",
"summer",
"tongue",
"accept",
"crazy",
"everyday",
"exist",
"grass",
"mistake",
"sent",
"shut",
"surround",
"table",
"ache",
"brain",
"destroy",
"heal",
"nature",
"shout",
"sign",
"stain",
"choice",
"doubt",
"glance",
"glow",
"mountain",
"queen",
"stranger",
"throat",
"tomorrow",
"city",
"either",
"fish",
"flame",
"rather",
"shape",
"spin",
"spread",
"ash",
"distance",
"finish",
"image",
"imagine",
"important",
"nobody",
"shatter",
"warmth",
"became",
"feed",
"flesh",
"funny",
"lust",
"shirt",
"trouble",
"yellow",
"attention",
"bare",
"bite",
"money",
"protect",
"amaze",
"appear",
"born",
"choke",
"completely",
"daughter",
"fresh",
"friendship",
"gentle",
"probably",
"six",
"deserve",
"expect",
"grab",
"middle",
"nightmare",
"river",
"thousand",
"weight",
"worst",
"wound",
"barely",
"bottle",
"cream",
"regret",
"relationship",
"stick",
"test",
"crush",
"endless",
"fault",
"itself",
"rule",
"spill",
"art",
"circle",
"join",
"kick",
"mask",
"master",
"passion",
"quick",
"raise",
"smooth",
"unless",
"wander",
"actually",
"broke",
"chair",
"deal",
"favorite",
"gift",
"note",
"number",
"sweat",
"box",
"chill",
"clothes",
"lady",
"mark",
"park",
"poor",
"sadness",
"tie",
"animal",
"belong",
"brush",
"consume",
"dawn",
"forest",
"innocent",
"pen",
"pride",
"stream",
"thick",
"clay",
"complete",
"count",
"draw",
"faith",
"press",
"silver",
"struggle",
"surface",
"taught",
"teach",
"wet",
"bless",
"chase",
"climb",
"enter",
"letter",
"melt",
"metal",
"movie",
"stretch",
"swing",
"vision",
"wife",
"beside",
"crash",
"forgot",
"guide",
"haunt",
"joke",
"knock",
"plant",
"pour",
"prove",
"reveal",
"steal",
"stuff",
"trip",
"wood",
"wrist",
"bother",
"bottom",
"crawl",
"crowd",
"fix",
"forgive",
"frown",
"grace",
"loose",
"lucky",
"party",
"release",
"surely",
"survive",
"teacher",
"gently",
"grip",
"speed",
"suicide",
"travel",
"treat",
"vein",
"written",
"cage",
"chain",
"conversation",
"date",
"enemy",
"however",
"interest",
"million",
"page",
"pink",
"proud",
"sway",
"themselves",
"winter",
"church",
"cruel",
"cup",
"demon",
"experience",
"freedom",
"pair",
"pop",
"purpose",
"respect",
"shoot",
"softly",
"state",
"strange",
"bar",
"birth",
"curl",
"dirt",
"excuse",
"lord",
"lovely",
"monster",
"order",
"pack",
"pants",
"pool",
"scene",
"seven",
"shame",
"slide",
"ugly",
"among",
"blade",
"blonde",
"closet",
"creek",
"deny",
"drug",
"eternity",
"gain",
"grade",
"handle",
"key",
"linger",
"pale",
"prepare",
"swallow",
"swim",
"tremble",
"wheel",
"won",
"cast",
"cigarette",
"claim",
"college",
"direction",
"dirty",
"gather",
"ghost",
"hundred",
"loss",
"lung",
"orange",
"present",
"swear",
"swirl",
"twice",
"wild",
"bitter",
"blanket",
"doctor",
"everywhere",
"flash",
"grown",
"knowledge",
"numb",
"pressure",
"radio",
"repeat",
"ruin",
"spend",
"unknown",
"buy",
"clock",
"devil",
"early",
"false",
"fantasy",
"pound",
"precious",
"refuse",
"sheet",
"teeth",
"welcome",
"add",
"ahead",
"block",
"bury",
"caress",
"content",
"depth",
"despite",
"distant",
"marry",
"purple",
"threw",
"whenever",
"bomb",
"dull",
"easily",
"grasp",
"hospital",
"innocence",
"normal",
"receive",
"reply",
"rhyme",
"shade",
"someday",
"sword",
"toe",
"visit",
"asleep",
"bought",
"center",
"consider",
"flat",
"hero",
"history",
"ink",
"insane",
"muscle",
"mystery",
"pocket",
"reflection",
"shove",
"silently",
"smart",
"soldier",
"spot",
"stress",
"train",
"type",
"view",
"whether",
"bus",
"energy",
"explain",
"holy",
"hunger",
"inch",
"magic",
"mix",
"noise",
"nowhere",
"prayer",
"presence",
"shock",
"snap",
"spider",
"study",
"thunder",
"trail",
"admit",
"agree",
"bag",
"bang",
"bound",
"butterfly",
"cute",
"exactly",
"explode",
"familiar",
"fold",
"further",
"pierce",
"reflect",
"scent",
"selfish",
"sharp",
"sink",
"spring",
"stumble",
"universe",
"weep",
"women",
"wonderful",
"action",
"ancient",
"attempt",
"avoid",
"birthday",
"branch",
"chocolate",
"core",
"depress",
"drunk",
"especially",
"focus",
"fruit",
"honest",
"match",
"palm",
"perfectly",
"pillow",
"pity",
"poison",
"roar",
"shift",
"slightly",
"thump",
"truck",
"tune",
"twenty",
"unable",
"wipe",
"wrote",
"coat",
"constant",
"dinner",
"drove",
"egg",
"eternal",
"flight",
"flood",
"frame",
"freak",
"gasp",
"glad",
"hollow",
"motion",
"peer",
"plastic",
"root",
"screen",
"season",
"sting",
"strike",
"team",
"unlike",
"victim",
"volume",
"warn",
"weird",
"attack",
"await",
"awake",
"built",
"charm",
"crave",
"despair",
"fought",
"grant",
"grief",
"horse",
"limit",
"message",
"ripple",
"sanity",
"scatter",
"serve",
"split",
"string",
"trick",
"annoy",
"blur",
"boat",
"brave",
"clearly",
"cling",
"connect",
"fist",
"forth",
"imagination",
"iron",
"jock",
"judge",
"lesson",
"milk",
"misery",
"nail",
"naked",
"ourselves",
"poet",
"possible",
"princess",
"sail",
"size",
"snake",
"society",
"stroke",
"torture",
"toss",
"trace",
"wise",
"bloom",
"bullet",
"cell",
"check",
"cost",
"darling",
"during",
"footstep",
"fragile",
"hallway",
"hardly",
"horizon",
"invisible",
"journey",
"midnight",
"mud",
"nod",
"pause",
"relax",
"shiver",
"sudden",
"value",
"youth",
"abuse",
"admire",
"blink",
"breast",
"bruise",
"constantly",
"couple",
"creep",
"curve",
"difference",
"dumb",
"emptiness",
"gotta",
"honor",
"plain",
"planet",
"recall",
"rub",
"ship",
"slam",
"soar",
"somebody",
"tightly",
"weather",
"adore",
"approach",
"bond",
"bread",
"burst",
"candle",
"coffee",
"cousin",
"crime",
"desert",
"flutter",
"frozen",
"grand",
"heel",
"hello",
"language",
"level",
"movement",
"pleasure",
"powerful",
"random",
"rhythm",
"settle",
"silly",
"slap",
"sort",
"spoken",
"steel",
"threaten",
"tumble",
"upset",
"aside",
"awkward",
"bee",
"blank",
"board",
"button",
"card",
"carefully",
"complain",
"crap",
"deeply",
"discover",
"drag",
"dread",
"effort",
"entire",
"fairy",
"giant",
"gotten",
"greet",
"illusion",
"jeans",
"leap",
"liquid",
"march",
"mend",
"nervous",
"nine",
"replace",
"rope",
"spine",
"stole",
"terror",
"accident",
"apple",
"balance",
"boom",
"childhood",
"collect",
"demand",
"depression",
"eventually",
"faint",
"glare",
"goal",
"group",
"honey",
"kitchen",
"laid",
"limb",
"machine",
"mere",
"mold",
"murder",
"nerve",
"painful",
"poetry",
"prince",
"rabbit",
"shelter",
"shore",
"shower",
"soothe",
"stair",
"steady",
"sunlight",
"tangle",
"tease",
"treasure",
"uncle",
"begun",
"bliss",
"canvas",
"cheer",
"claw",
"clutch",
"commit",
"crimson",
"crystal",
"delight",
"doll",
"existence",
"express",
"fog",
"football",
"gay",
"goose",
"guard",
"hatred",
"illuminate",
"mass",
"math",
"mourn",
"rich",
"rough",
"skip",
"stir",
"student",
"style",
"support",
"thorn",
"tough",
"yard",
"yearn",
"yesterday",
"advice",
"appreciate",
"autumn",
"bank",
"beam",
"bowl",
"capture",
"carve",
"collapse",
"confusion",
"creation",
"dove",
"feather",
"girlfriend",
"glory",
"government",
"harsh",
"hop",
"inner",
"loser",
"moonlight",
"neighbor",
"neither",
"peach",
"pig",
"praise",
"screw",
"shield",
"shimmer",
"sneak",
"stab",
"subject",
"throughout",
"thrown",
"tower",
"twirl",
"wow",
"army",
"arrive",
"bathroom",
"bump",
"cease",
"cookie",
"couch",
"courage",
"dim",
"guilt",
"howl",
"hum",
"husband",
"insult",
"led",
"lunch",
"mock",
"mostly",
"natural",
"nearly",
"needle",
"nerd",
"peaceful",
"perfection",
"pile",
"price",
"remove",
"roam",
"sanctuary",
"serious",
"shiny",
"shook",
"sob",
"stolen",
"tap",
"vain",
"void",
"warrior",
"wrinkle",
"affection",
"apologize",
"blossom",
"bounce",
"bridge",
"cheap",
"crumble",
"decision",
"descend",
"desperately",
"dig",
"dot",
"flip",
"frighten",
"heartbeat",
"huge",
"lazy",
"lick",
"odd",
"opinion",
"process",
"puzzle",
"quietly",
"retreat",
"score",
"sentence",
"separate",
"situation",
"skill",
"soak",
"square",
"stray",
"taint",
"task",
"tide",
"underneath",
"veil",
"whistle",
"anywhere",
"bedroom",
"bid",
"bloody",
"burden",
"careful",
"compare",
"concern",
"curtain",
"decay",
"defeat",
"describe",
"double",
"dreamer",
"driver",
"dwell",
"evening",
"flare",
"flicker",
"grandma",
"guitar",
"harm",
"horrible",
"hungry",
"indeed",
"lace",
"melody",
"monkey",
"nation",
"object",
"obviously",
"rainbow",
"salt",
"scratch",
"shown",
"shy",
"stage",
"stun",
"third",
"tickle",
"useless",
"weakness",
"worship",
"worthless",
"afternoon",
"beard",
"boyfriend",
"bubble",
"busy",
"certain",
"chin",
"concrete",
"desk",
"diamond",
"doom",
"drawn",
"due",
"felicity",
"freeze",
"frost",
"garden",
"glide",
"harmony",
"hopefully",
"hunt",
"jealous",
"lightning",
"mama",
"mercy",
"peel",
"physical",
"position",
"pulse",
"punch",
"quit",
"rant",
"respond",
"salty",
"sane",
"satisfy",
"savior",
"sheep",
"slept",
"social",
"sport",
"tuck",
"utter",
"valley",
"wolf",
"aim",
"alas",
"alter",
"arrow",
"awaken",
"beaten",
"belief",
"brand",
"ceiling",
"cheese",
"clue",
"confidence",
"connection",
"daily",
"disguise",
"eager",
"erase",
"essence",
"everytime",
"expression",
"fan",
"flag",
"flirt",
"foul",
"fur",
"giggle",
"glorious",
"ignorance",
"law",
"lifeless",
"measure",
"mighty",
"muse",
"north",
"opposite",
"paradise",
"patience",
"patient",
"pencil",
"petal",
"plate",
"ponder",
"possibly",
"practice",
"slice",
"spell",
"stock",
"strife",
"strip",
"suffocate",
"suit",
"tender",
"tool",
"trade",
"velvet",
"verse",
"waist",
"witch",
"aunt",
"bench",
"bold",
"cap",
"certainly",
"click",
"companion",
"creator",
"dart",
"delicate",
"determine",
"dish",
"dragon",
"drama",
"drum",
"dude",
"everybody",
"feast",
"forehead",
"former",
"fright",
"fully",
"gas",
"hook",
"hurl",
"invite",
"juice",
"manage",
"moral",
"possess",
"raw",
"rebel",
"royal",
"scale",
"scary",
"several",
"slight",
"stubborn",
"swell",
"talent",
"tea",
"terrible",
"thread",
"torment",
"trickle",
"usually",
"vast",
"violence",
"weave",
"acid",
"agony",
"ashamed",
"awe",
"belly",
"blend",
"blush",
"character",
"cheat",
"common",
"company",
"coward",
"creak",
"danger",
"deadly",
"defense",
"define",
"depend",
"desperate",
"destination",
"dew",
"duck",
"dusty",
"embarrass",
"engine",
"example",
"explore",
"foe",
"freely",
"frustrate",
"generation",
"glove",
"guilty",
"health",
"hurry",
"idiot",
"impossible",
"inhale",
"jaw",
"kingdom",
"mention",
"mist",
"moan",
"mumble",
"mutter",
"observe",
"ode",
"pathetic",
"pattern",
"pie",
"prefer",
"puff",
"rape",
"rare",
"revenge",
"rude",
"scrape",
"spiral",
"squeeze",
"strain",
"sunset",
"suspend",
"sympathy",
"thigh",
"throne",
"total",
"unseen",
"weapon",
"weary"
]

# http://en.wiktionary.org/wiki/Appendix:Frequency_dictionary_of_the_modern_Russian_language_%28the_Russian_National_Corpus%29

words_ru = [
"и",
"в",
"не",
"на",
"я",
"быть",
"он",
"с",
"что",
"а",
"по",
"это",
"она",
"этот",
"к",
"но",
"они",
"мы",
"как",
"из",
"у",
"который",
"то",
"за",
"свой",
"что",
"весь",
"год",
"от",
"так",
"о",
"для",
"ты",
"же",
"все",
"тот",
"мочь",
"вы",
"человек",
"такой",
"его",
"сказать",
"только",
"или",
"еще",
"бы",
"себя",
"один",
"как",
"уже",
"до",
"время",
"если",
"сам",
"когда",
"другой",
"вот",
"говорить",
"наш",
"мой",
"знать",
"стать",
"при",
"чтобы",
"дело",
"жизнь",
"кто",
"первый",
"очень",
"два",
"день",
"ее",
"новый",
"рука",
"даже",
"во",
"со",
"раз",
"где",
"там",
"под",
"можно",
"ну",
"какой",
"после",
"их",
"работа",
"без",
"самый",
"потом",
"надо",
"хотеть",
"ли",
"слово",
"идти",
"большой",
"должен",
"место",
"иметь",
"ничто",
"то",
"сейчас",
"тут",
"лицо",
"каждый",
"друг",
"нет",
"теперь",
"ни",
"глаз",
"тоже",
"тогда",
"видеть",
"вопрос",
"через",
"да",
"здесь",
"дом",
"да",
"потому",
"сторона",
"какой-то",
"думать",
"сделать",
"страна",
"жить",
"чем",
"мир",
"об",
"последний",
"случай",
"голова",
"более",
"делать",
"что-то",
"смотреть",
"ребенок",
"просто",
"конечно",
"сила",
"российский",
"конец",
"перед",
"несколько",
"вид",
"система",
"всегда",
"работать",
"между",
"три",
"нет",
"понять",
"пойти",
"часть",
"спросить",
"город",
"дать",
"также",
"никто",
"понимать",
"получить",
"отношение",
"лишь",
"второй",
"именно",
"ваш",
"хотя",
"ни",
"сидеть",
"над",
"женщина",
"оказаться",
"русский",
"один",
"взять",
"прийти",
"являться",
"деньги",
"почему",
"вдруг",
"любить",
"стоить",
"почти",
"земля",
"общий",
"ведь",
"машина",
"однако",
"сразу",
"хорошо",
"вода",
"отец",
"высокий",
"остаться",
"выйти",
"много",
"проблема",
"начать",
"хороший",
"час",
"это",
"сегодня",
"право",
"совсем",
"нога",
"считать",
"главный",
"решение",
"увидеть",
"дверь",
"казаться",
"образ",
"писать",
"история",
"лучший",
"власть",
"закон",
"все",
"война",
"бог",
"голос",
"найти",
"поэтому",
"стоять",
"вообще",
"тысяча",
"больше",
"вместе",
"маленький",
"книга",
"некоторый",
"решить",
"любой",
"возможность",
"результат",
"ночь",
"стол",
"никогда",
"имя",
"область",
"молодой",
"пройти",
"например",
"статья",
"оно",
"число",
"компания",
"про",
"государственный",
"полный",
"принять",
"народ",
"никакой",
"советский",
"жена",
"настоящий",
"всякий",
"группа",
"развитие",
"процесс",
"суд",
"давать",
"ответить",
"старый",
"условие",
"твой",
"пока",
"средство",
"помнить",
"начало",
"ждать",
"свет",
"пора",
"путь",
"душа",
"куда",
"нужно",
"разный",
"нужный",
"уровень",
"иной",
"форма",
"связь",
"уж",
"минута",
"кроме",
"находиться",
"опять",
"многий",
"белый",
"собственный",
"улица",
"черный",
"написать",
"вечер",
"снова",
"основной",
"качество",
"мысль",
"дорога",
"мать",
"действие",
"месяц",
"оставаться",
"государство",
"язык",
"любовь",
"взгляд",
"мама",
"играть",
"далекий",
"лежать",
"нельзя",
"век",
"школа",
"подумать",
"уйти",
"цель",
"среди",
"общество",
"посмотреть",
"деятельность",
"организация",
"кто-то",
"вернуться",
"президент",
"комната",
"порядок",
"момент",
"театр",
"следовать",
"читать",
"письмо",
"подобный",
"следующий",
"утро",
"особенно",
"помощь",
"ситуация",
"роль",
"бывать",
"ходить",
"рубль",
"начинать",
"появиться",
"смысл",
"состояние",
"называть",
"рядом",
"квартира",
"назад",
"равный",
"из-за",
"орган",
"внимание",
"тело",
"труд",
"прийтись",
"хотеться",
"сын",
"мера",
"пять",
"смерть",
"живой",
"рынок",
"программа",
"задача",
"предприятие",
"известный",
"окно",
"вести",
"совершенно",
"военный",
"разговор",
"показать",
"правительство",
"важный",
"семья",
"великий",
"производство",
"простой",
"значит",
"третий",
"сколько",
"огромный",
"давно",
"политический",
"информация",
"действительно",
"положение",
"поставить",
"бояться",
"наконец",
"центр",
"происходить",
"ответ",
"муж",
"автор",
"все-таки",
"стена",
"существовать",
"даже",
"интерес",
"становиться",
"федерация",
"правило",
"оба",
"часто",
"московский",
"управление",
"слышать",
"быстро",
"смочь",
"заметить",
"как-то",
"мужчина",
"долго",
"правда",
"идея",
"партия",
"иногда",
"использовать",
"пытаться",
"готовый",
"чуть",
"зачем",
"представить",
"чувствовать",
"создать",
"совет",
"счет",
"сердце",
"движение",
"вещь",
"материал",
"неделя",
"чувство",
"затем",
"данный",
"заниматься",
"продолжать",
"красный",
"глава",
"ко",
"слушать",
"наука",
"узнать",
"ряд",
"газета",
"причина",
"против",
"плечо",
"современный",
"цена",
"план",
"приехать",
"речь",
"четыре",
"отвечать",
"точка",
"основа",
"товарищ",
"культура",
"слишком",
"рассказывать",
"вполне",
"далее",
"рассказать",
"данные",
"представлять",
"мнение",
"социальный",
"около",
"документ",
"институт",
"ход",
"брать",
"забыть",
"проект",
"ранний",
"встреча",
"особый",
"целый",
"директор",
"провести",
"спать",
"плохой",
"может",
"впрочем",
"сильный",
"наверное",
"скорый",
"ведь",
"срок",
"палец",
"опыт",
"помочь",
"больше",
"приходить",
"служба",
"крупный",
"внутренний",
"просить",
"вспомнить",
"открыть",
"привести",
"судьба",
"пока",
"девушка",
"поскольку",
"очередь",
"лес",
"пусть",
"экономический",
"оставить",
"правый",
"состав",
"словно",
"федеральный",
"спрашивать",
"принимать",
"член",
"искать",
"близкий",
"количество",
"похожий",
"событие",
"объект",
"зал",
"создание",
"войти",
"различный",
"значение",
"назвать",
"достаточно",
"период",
"хоть",
"шаг",
"необходимый",
"успеть",
"произойти",
"брат",
"искусство",
"единственный",
"легкий",
"структура",
"выходить",
"номер",
"предложить",
"пример",
"пить",
"исследование",
"гражданин",
"глядеть",
"человеческий",
"игра",
"начальник",
"сей",
"рост",
"ехать",
"международный",
"тема",
"принцип",
"дорогой",
"попасть",
"десять",
"начаться",
"верить",
"метод",
"тип",
"фильм",
"небольшой",
"держать",
"либо",
"позволять",
"край",
"местный",
"менее",
"гость",
"купить",
"уходить",
"собираться",
"воздух",
"туда",
"относиться",
"бывший",
"требовать",
"характер",
"борьба",
"использование",
"кстати",
"подойти",
"размер",
"удаться",
"образование",
"получать",
"мальчик",
"кровь",
"район",
"небо",
"американский",
"армия",
"класс",
"представитель",
"участие",
"девочка",
"политика",
"сначала",
"герой",
"картина",
"широкий",
"доллар",
"спина",
"территория",
"мировой",
"пол",
"тяжелый",
"довольно",
"поле",
"ж",
"изменение",
"умереть",
"более",
"направление",
"рисунок",
"течение",
"возможный",
"церковь",
"банк",
"отдельный",
"средний",
"красивый",
"сцена",
"население",
"большинство",
"сесть",
"двадцать",
"случиться",
"музыка",
"короткий",
"правда",
"проходить",
"составлять",
"свобода",
"память",
"приходиться",
"причем",
"команда",
"установить",
"союз",
"будто",
"поднять",
"врач",
"серьезный",
"договор",
"стараться",
"уметь",
"встать",
"дерево",
"интересный",
"факт",
"добрый",
"всего",
"хозяин",
"национальный",
"однажды",
"длинный",
"природа",
"домой",
"страшный",
"прошлый",
"будто",
"общественный",
"угол",
"чтоб",
"телефон",
"позиция",
"проводить",
"скоро",
"наиболее",
"двор",
"обычно",
"бросить",
"разве",
"писатель",
"самолет",
"объем",
"далеко",
"род",
"солнце",
"вера",
"берег",
"спектакль",
"фирма",
"способ",
"завод",
"цвет",
"трудно",
"журнал",
"руководитель",
"специалист",
"возможно",
"детский",
"точно",
"объяснить",
"оценка",
"единый",
"снять",
"определенный",
"низкий",
"нравиться",
"услышать",
"регион",
"связать",
"песня",
"процент",
"родитель",
"позволить",
"чужой",
"море",
"странный",
"требование",
"чистый",
"весьма",
"какой-нибудь",
"основание",
"половина",
"поехать",
"положить",
"входить",
"легко",
"поздний",
"роман",
"круг",
"анализ",
"стихи",
"автомобиль",
"специальный",
"экономика",
"литература",
"бумага",
"вместо",
"впервые",
"видно",
"научный",
"оказываться",
"поэт",
"показывать",
"степень",
"вызвать",
"касаться",
"господин",
"надежда",
"сложный",
"вокруг",
"предмет",
"отметить",
"заявить",
"вариант",
"министр",
"откуда",
"реальный",
"граница",
"действовать",
"дух",
"модель",
"операция",
"пара",
"сон",
"немного",
"название",
"ум",
"повод",
"старик",
"способный",
"мало",
"миллион",
"малый",
"старший",
"успех",
"практически",
"получиться",
"личный",
"счастье",
"необходимо",
"свободный",
"ребята",
"обычный",
"кабинет",
"прекрасный",
"высший",
"кричать",
"прежде",
"магазин",
"пространство",
"выход",
"остановиться",
"удар",
"база",
"знание",
"текст",
"сюда",
"темный",
"защита",
"предлагать",
"руководство",
"вовсе",
"площадь",
"сознание",
"гражданский",
"убить",
"возраст",
"молчать",
"согласиться",
"участник",
"участок",
"рано",
"пункт",
"несмотря",
"сильно",
"столь",
"сообщить",
"линия",
"бежать",
"желание",
"папа",
"кажется",
"петь",
"доктор",
"губа",
"известно",
"дома",
"вызывать",
"дочь",
"показаться",
"среда",
"председатель",
"представление",
"солдат",
"художник",
"принести",
"волос",
"оружие",
"выглядеть",
"соответствие",
"никак",
"ветер",
"внешний",
"парень",
"служить",
"зрение",
"попросить",
"генерал",
"состоять",
"огонь",
"отдать",
"боевой",
"понятие",
"строительство",
"ухо",
"выступать",
"грудь",
"нос",
"ставить",
"завтра",
"возникать",
"когда",
"страх",
"услуга",
"рабочий",
"что-нибудь",
"глубокий",
"содержание",
"радость",
"безопасность",
"надеяться",
"продукт",
"видимо",
"комплекс",
"бизнес",
"подняться",
"вспоминать",
"мало",
"сад",
"долгий",
"одновременно",
"называться",
"сотрудник",
"лето",
"тихо",
"зато",
"прямой",
"курс",
"помогать",
"предложение",
"финансовый",
"открытый",
"почему-то",
"значить",
"возникнуть",
"рот",
"где-то",
"технология",
"знакомый",
"недавно",
"реформа",
"отсутствие",
"нынешний",
"собака",
"камень",
"будущее",
"звать",
"рассказ",
"контроль",
"позвонить",
"река",
"хватать",
"продукция",
"сумма",
"техника",
"исторический",
"вновь",
"народный",
"прямо",
"ибо",
"выпить",
"здание",
"сфера",
"знаменитый",
"иначе",
"потерять",
"необходимость",
"больший",
"фонд",
"иметься",
"вперед",
"подготовка",
"вчера",
"лист",
"пустой",
"очередной",
"республика",
"хозяйство",
"полностью",
"получаться",
"учиться",
"плохо",
"воля",
"судебный",
"бюджет",
"возвращаться",
"расти",
"снег",
"деревня",
"обнаружить",
"мужик",
"постоянно",
"зеленый",
"элемент",
"обстоятельство",
"почувствовать",
"немец",
"многое",
"победа",
"источник",
"немецкий",
"золотой",
"передать",
"технический",
"нормальный",
"едва",
"желать",
"ожидать",
"некий",
"звезда",
"городской",
"выбор",
"соответствующий",
"масса",
"составить",
"итог",
"сестра",
"что",
"шесть",
"ясно",
"практика",
"сто",
"нести",
"определить",
"проведение",
"карман",
"любимый",
"родной",
"западный",
"обязательно",
"слава",
"кухня",
"определение",
"пользоваться",
"быстрый",
"функция",
"войско",
"комиссия",
"применение",
"капитан",
"работник",
"улыбнуться",
"холодный",
"обеспечение",
"офицер",
"появляться",
"конкретный",
"фамилия",
"предел",
"прямо",
"смеяться",
"выборы",
"иностранный",
"уехать",
"ученый",
"вроде",
"левый",
"счастливый",
"бутылка",
"бой",
"подходить",
"судить",
"родиться",
"теория",
"зона",
"отдел",
"зуб",
"разработка",
"отказаться",
"святой",
"считаться",
"точный",
"занять",
"личность",
"гора",
"добавить",
"товар",
"звонить",
"медленно",
"носить",
"метр",
"начинаться",
"зависеть",
"праздник",
"влияние",
"построить",
"читатель",
"частый",
"удовольствие",
"актер",
"слеза",
"создавать",
"значительный",
"ответственность",
"учитель",
"акт",
"встретить",
"принадлежать",
"произнести",
"боль",
"множество",
"связанный",
"особенность",
"участвовать",
"показатель",
"занимать",
"корабль",
"уверенный",
"звук",
"тонкий",
"центральный",
"впечатление",
"спокойно",
"частность",
"детство",
"вывод",
"профессор",
"будущий",
"доля",
"норма",
"улыбаться",
"прошлое",
"возле",
"командир",
"коридор",
"поддержка",
"рамка",
"вскоре",
"лучше",
"сквозь",
"враг",
"ладно",
"этап",
"черт",
"дед",
"направить",
"собрание",
"прием",
"физический",
"болезнь",
"клетка",
"кожа",
"заявление",
"ради",
"попытка",
"сравнение",
"только",
"расчет",
"когда-то",
"депутат",
"то",
"частный",
"обратиться",
"мелкий",
"невозможно",
"английский",
"постоянный",
"комитет",
"знак",
"выбрать",
"примерно",
"бить",
"дядя",
"учет",
"хлеб",
"тихий",
"хватить",
"обещать",
"ли",
"встречаться",
"чай",
"режим",
"целое",
"вирус",
"гораздо",
"тридцать",
"выражение",
"напоминать",
"уж",
"неожиданно",
"здоровье",
"зима",
"упасть",
"перестать",
"десяток",
"глубина",
"сеть",
"студент",
"обладать",
"секунда",
"скорость",
"поиск",
"европейский",
"суть",
"налог",
"ошибка",
"ближайший",
"отечественный",
"теплый",
"плакать",
"духовный",
"доход",
"прежний",
"режиссер",
"поверхность",
"ощущение",
"состояться",
"карта",
"клуб",
"семь",
"станция",
"революция",
"колено",
"министерство",
"стекло",
"этаж",
"остальной",
"высота",
"наоборот",
"бабушка",
"двое",
"поверить",
"трубка",
"собрать",
"профессиональный",
"французский",
"женский",
"крайний",
"простить",
"газ",
"естественно",
"мастер",
"вниз",
"главное",
"поведение",
"рассматривать",
"перейти",
"мешать",
"давай",
"столица",
"механизм",
"передача",
"божий",
"исчезнуть",
"способность",
"подход",
"разумеется",
"столько",
"энергия",
"дальнейший",
"существование",
"исполнение",
"сорок",
"кино",
"сожаление",
"заместитель",
"мол",
"объявить",
"отличаться",
"естественный",
"ресурс",
"обращаться",
"акция",
"информационный",
"рождение",
"снимать",
"явно",
"администрация",
"железный",
"пригласить",
"соответствовать",
"стоимость",
"улыбка",
"артист",
"горячий",
"закрыть",
"придумать",
"пожалуйста",
"попробовать",
"приводить",
"сосед",
"фраза",
"веселый",
"фигура",
"достигнуть",
"субъект",
"утверждать",
"реакция",
"список",
"фотография",
"журналист",
"май",
"означать",
"платить",
"нарушение",
"заседание",
"толпа",
"больница",
"существо",
"решать",
"интересно",
"официальный",
"свойство",
"долг",
"поколение",
"серый",
"животное",
"схема",
"усилие",
"отличие",
"опасный",
"определять",
"остров",
"наблюдать",
"противник",
"волна",
"погибнуть",
"разговаривать",
"прочий",
"реализация",
"страница",
"формирование",
"житель",
"устроить",
"есть",
"красота",
"правильно",
"благодаря",
"птица",
"собраться",
"достать",
"растение",
"тень",
"явление",
"храм",
"запах",
"слабый",
"водка",
"наличие",
"пожалуй",
"яркий",
"ужас",
"одежда",
"ездить",
"кресло",
"больной",
"поезд",
"университет",
"летний",
"дополнительный",
"понравиться",
"традиция",
"адрес",
"декабрь",
"ладонь",
"поздно",
"сведение",
"правильный",
"цветок",
"выполнять",
"лесной",
"лидер",
"октябрь",
"занятие",
"заставить",
"объяснять",
"сентябрь",
"помещение",
"прочее",
"согласно",
"январь",
"выполнить",
"зритель",
"постепенно",
"резко",
"редакция",
"указать",
"умный",
"стиль",
"весна",
"северный",
"фактор",
"август",
"известие",
"зависимость",
"охрана",
"ясный",
"милый",
"оборудование",
"светлый",
"концерт",
"отделение",
"расход",
"редкий",
"выставка",
"милиция",
"верный",
"вздохнуть",
"юридический",
"находить",
"переход",
"закончить",
"эпоха",
"запад",
"признать",
"произведение",
"родина",
"собственность",
"тайна",
"хотя",
"четвертый",
"административный",
"трава",
"дойти",
"лагерь",
"во-первых",
"имущество",
"кивнуть",
"кровать",
"понятно",
"настолько",
"обратить",
"узкий",
"абсолютно",
"аппарат",
"несколько",
"очевидно",
"середина",
"узнавать",
"встретиться",
"март",
"художественный",
"клиент",
"лично",
"дама",
"обратно",
"предусмотреть",
"фронт",
"древний",
"отрасль",
"стул",
"беседа",
"массовый",
"обеспечивать",
"генеральный",
"замечательный",
"хоть",
"двигаться",
"законодательство",
"продажа",
"повышение",
"содержать",
"страшно",
"прежде",
"музей",
"задний",
"региональный",
"след",
"из-под",
"полковник",
"приезжать",
"сомнение",
"понимание",
"здоровый",
"держаться",
"обеспечить",
"слегка",
"апрель",
"князь",
"поступить",
"рыба",
"привыкнуть",
"активный",
"литературный",
"открывать",
"собственно",
"дума",
"еще",
"неужели",
"кодекс",
"сутки",
"чудо",
"вырасти",
"шея",
"зайти",
"судья",
"острый",
"посвятить",
"стремиться",
"богатый",
"крыша",
"настроение",
"отсюда",
"творческий",
"нечто",
"поток",
"мягкий",
"ночной",
"должность",
"преступление",
"измениться",
"мозг",
"налоговый",
"толстый",
"честь",
"пост",
"удивиться",
"падать",
"еврей",
"звучать",
"бедный",
"июнь",
"много",
"сотня",
"верхний",
"суметь",
"вечный",
"восемь",
"лишний",
"морской",
"разработать",
"нижний",
"спокойный",
"поговорить",
"дождь",
"меньше",
"лестница",
"сухой",
"ах",
"лететь",
"совершить",
"дача",
"синий",
"просто",
"установка",
"появление",
"получение",
"сегодняшний",
"строить",
"образец",
"труба",
"главное",
"кончиться",
"медицинский",
"привезти",
"многие",
"осень",
"вряд",
"сложиться",
"оставлять",
"полагать",
"висеть",
"костюм",
"свежий",
"трудный",
"уголовный",
"баба",
"ценность",
"обязанность",
"пьеса",
"чей",
"таблица",
"вино",
"воспоминание",
"лошадь",
"повторить",
"кто-нибудь",
"сыграть",
"коллега",
"организм",
"случайно",
"ученик",
"учреждение",
"высоко",
"открытие",
"спасти",
"том",
"черта",
"изменить",
"повторять",
"характеристика",
"по-прежнему",
"явиться",
"выполнение",
"оборона",
"выступление",
"температура",
"замечать",
"перспектива",
"подать",
"подруга",
"приказ",
"вверх",
"жертва",
"назначить",
"протянуть",
"ресторан",
"километр",
"сохранить",
"спор",
"попытаться",
"расположить",
"использоваться",
"вкус",
"насколько",
"признак",
"промышленность",
"странно",
"американец",
"лоб",
"заключение",
"вероятно",
"восток",
"вроде",
"исключение",
"отправиться",
"желтый",
"молча",
"ключ",
"постановление",
"садиться",
"же",
"немедленно",
"слой",
"бок",
"встречать",
"говориться",
"крикнуть",
"спустя",
"июль",
"мощный",
"перевод",
"секретарь",
"кусок",
"готовить",
"слух",
"учить",
"гореть",
"испытывать",
"польза",
"звонок",
"выделить",
"обстановка",
"оттуда",
"мимо",
"поддерживать",
"подниматься",
"чиновник",
"следить",
"соглашение",
"деталь",
"русский",
"деревянный",
"тишина",
"зарплата",
"требоваться",
"билет",
"включать",
"подарок",
"тюрьма",
"ящик",
]

words = words_en

n = 1626

# Note about US patent no 5892470: Here each word does not represent a given digit.
# Instead, the digit represented by a word is variable, it depends on the previous word.

def mn_encode( message ):
    out = []
    for i in range(len(message)//8):
        word = message[8*i:8*i+8]
        x = int(word, 16)
        w1 = (x%n)
        w2 = ((x//n) + w1)%n
        w3 = ((x//n//n) + w2)%n
        out += [ words[w1], words[w2], words[w3] ]
    return out

def mn_decode( wlist ):
    out = ''
    for i in range(len(wlist)//3):
        word1, word2, word3 = wlist[3*i:3*i+3]
        w1 =  words.index(word1)
        w2 = (words.index(word2))%n
        w3 = (words.index(word3))%n
        x = w1 +n*((w2-w1)%n) +n*n*((w3-w2)%n)
        out += '%08x'%x
    return out

def hex2mnemonic(value):
    return ' '.join(mn_encode(value))

if __name__ == '__main__':
    import sys
    BITS = 256
    if len(sys.argv) >= 2 and sys.argv[1] == 'ru':
        words = words_ru
        del sys.argv[1]
    if len(sys.argv) >= 2 and sys.argv[1] == '128':
        BITS = 128
        del sys.argv[1]
    if len( sys.argv ) == 1:
        print('Usage: mnemonic.py [ru] [128] random|hex-string|mnemonic')
    elif len( sys.argv ) == 2:
        if sys.argv[1] == 'random':
            import random
            chars = int(BITS / 8 * 2)
            ABC = '0123456789abcdef'
            value = ''.join(random.choice(ABC) for i in range(chars))
            print(value)
            print(hex2mnemonic(value))
        elif ' ' in sys.argv[1]:
            print(mn_decode(sys.argv[1].split()))
        else:
            print(hex2mnemonic(sys.argv[1]))
    else:
        print(mn_decode(sys.argv[1:]))
