def securehash(string): # Returns an unsigned 256-bit value.
    s = list(string)
    s.append('y')
    hashtable = {" ":3359021268240736195176116814970269849610326840826118994465753404115666980246,"!":41719877443921282727592877396977407073962805828339361978708640132710534145025,'"':91941850019847354222880053459001882925421039185972937973513163389924973660083,"#":22310553771286139412632513243762666804576608716639108490078938781349945543373,"$":33338808925653727818764142301670780277372960629885024052047999043307436183773,"%":76557746933240315928758827783175753396055952363681453779931993397714230364721,"&":77447100552163325377114726573327352006773650670137924970660451411582197008474,"\'":14466073093540817614718594905607551687751856205557160448490877593876624994191,"(":27182401998318407538349496857053645259548908245229490237708309654118506465806,")":30875895521404414287601597031669067262915076365238289994843428645039437732371,"*":67979251199642264090921044626486078374150549882476037788589922762464859461446,"+":114469230743164604573787565466037365598766797452163259590871885854194168594446,",":3076755195609789574411682107569680411692461290399736151038546247952292837947,"-":49663879259343194299412355683740742315424657073049051882221822307152934092540,".":6494050826384276888687485298422886562786755471532250625416658210571565256138,"/":105209612463218422310292626322401765715207106140047651319865294265146695778621,"0":101230680639367059983528506907585775727493050907262251533441786213132310858375,"1":87386069384936789197746897416088554568371443742277252575382249936286459892977,"2":70556569777364621566555813704968086083779355127857515186805819013124467905078,"3":45363685616516744141354462517262485041153920539658489921839927287601759305928,"4":8840768721232029505079764332813010004980010840902476680870080004423372509885,"5":37787269783638256488842799577168285756128538647156647590759341025060862569489,"6":49969697278241856725934390194422160306774760238871456726583996750633429132357,"7":8749069264248895033345768177697944463319412276411221988230104385867712013750,"8":113888557194212433646326729745747478768387399480421582448840286843132264167289,"9":20767067592297926978392315470235931417643398412654124972082239162395779480266,":":6841029758683401029137061913000544562450815171475549108943071006938664333157,";":62193291896105423681305487314492266879751494012836855588273274357529149332242,"<":71103100307102817813581634658998082277589503034191110332690031635769311781546,"=":20931737384789645543874564490140755410948926682372361653570661901479915914898,">":22247557091955276190147260495022557872485717303898654528546088984080740466476,"?":57220643753830031749479410784721845112543710576947062227765439635236887437954,"@":20509139714719857790652651214229281513382523246690312626389320215457009384473,"A":9838326942838317401854018783399979737051588061228154408071426228034708692427,"B":32059610341077934771501090919442856116502364907007793590110938535145456232122,"C":85791841208561755698460038182059456963347717623625943233345588785941714789836,"D":106965637715203578783896284122133972403462507603223854950028443057271268405096,"E":112593276766972863626790633652983215662574538572603983055692324431548291299604,"F":104140114542893935032876261291618000344940372628290036236473783392150712945605,"G":105963449105977243038466011672251367690171794692049575092297601169995036864514,"H":39015802499257141433581218804293975584266886473919294227293016972942429879440,"I":27034040850301679222397734918379080039611664043555709218215595160694141464372,"J":40405932759280373188472603121680889857420208532982661874823440593044291028975,"K":7940535126809568174910817702354604223588038876129466943305006610702172602174,"L":56840075464147732079117563506155864246947448735896410925311552002549463807009,"M":100244100065199072973388988839712296511570773609643095621945504802428537604924,"N":43001103226441847017130881458302930990861444065442663940885955296133377363836,"O":106346091076156128317423774377046373542711518198778488987174250063720049441603,"P":41232281350578260240829104095430712488803300582813553445376988431434812298601,"Q":1510372390709047078799557056892116936839938017673298103231784103008824222921,"R":38083183988629259078277418244115384182619417393515315357164873792283855624986,"S":111043357877302451551702308419498918988347718162875767828088094181685440478561,"T":94155003177699832934154825383510759649247995955213842992059066104687781145582,"U":83869928958859486543703457926159362464322530692138317656190710970288645014666,"V":18972713646896272112886016655652392002442627808041293583556653138905161569084,"W":104661434294296865834166625316074828860573956405328910300732271419331742699846,"X":102436980703786722171131620860896543624256752324619182229248137529995482847564,"Y":94469942682821654548988162005419530308707576559206561996996848280910309376598,"Z":67162349533454719458205913323757182839563568150772405804528959772517670122207,"[":55741672684115417489361768938038360923928259946807369754391873634618057094658,"\\":46144096196324970099936344553921996301823926080952313707931759943917502122477,"]":50850842325211156138884776235127814181957680142388410849848874588951621668507,"^":35640944271784335913352040414382988317429362535235146044770924016365124870427,"_":62636059408726471296092789605393523641863015590222328568161170068909665620184,"`":25785638016388785985745176543995829532453058957127994757120037191344160238410,"a":88940943573232407496465459701183009995666964112366442530509562134225641898682,"b":68579228565140479211854159683474892078796390143100061615903374326721932949805,"c":2729182896498466627308723164403823721599852986087312824424152168125616418232,"d":60917677137404307723328216564193185149185924125182813497421360662973221283788,"e":73296989673884726338928586441691742903979201923967634466358981291993263628069,"f":41481674916779187643424989381667139279543587935994324397246706776275890763156,"g":104493091305322854479039178115520772659413827708321344341645281628128996820417,"h":109909623089387438025643416889167242070759055760947073488499365692638348173098,"i":30059162318391758199676381043620848118065715877084665030316560759968922045176,"j":104867448529444689775331793596075598623806391948407940545455389048815175662614,"k":99682718518027772892342045433593246132679177005369076119501554601028395092111,"l":9361952585674946677719687237301337856449125852821468671277352472579682909263,"m":24730138933200207305028173768659952953989795357697997410159670103892948708523,"n":102592967781241451681428014678135304970454329067651845078859307824325963410479,"o":55536993381500017369468816596724736279296283813802356177791027003413308418190,"p":32041189012613020919137698945489926274164407444004888108041645409782455285194,"q":87933723788094650625657372125326851196405797642590248203632171513421287090470,"r":78963094941426017159814328758295534673957014865785609884312300187070279773482,"s":22122165933122394354608998254692582616320895125550423272082072324369783786633,"t":93175878573188357819515959352634807000656694801825938516916129333311360917093,"u":70747605958245317536580402908206023948592665883897929496459898710539905037707,"v":85271251774085251852003951381181684700163052772250112697637377753982001934439,"w":79191397938057110504953070401905413313050466338749260350665588825307423615052,"x":62789706580046388107417279887687184405295249255232882836500801774495524265096,"y":101121675074378967696024737646827384614347085585293539985237300119164024161301,"z":82693688807463617776930221951342985450202392457020019830996818730788867046113,"{":99096563524645718309357733921319978764396479242390678760682713381981886231390,"|":25972057629211796948618389662098928747051750997087155967038546763112483474653,"}":31482783485993433219234377134097878215113940049201767610825701166581899095627,"~":25487351017818062116926002614167557188863528236054140897853963608679386473666,}
    retval = 0
    for ind in s:
        for char in s:
            retval += hashtable[char]
        s.remove(ind)
    return retval%(2**256)


        
            
    