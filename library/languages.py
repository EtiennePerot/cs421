# -*- coding: utf-8 -*-

from base import *

languagesTable = dbTable("""CREATE TABLE `languages` (
  `iso` varchar(16) NOT NULL COMMENT 'ISO language code',
  `english` varchar(255) NOT NULL,
  `translated` varchar(255) NOT NULL,
  PRIMARY KEY (`iso`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
Language = languagesTable.genClass()

hasLanguagesTable = dbTable("""CREATE TABLE `has_languages` (
  `iid` int(10) unsigned NOT NULL COMMENT 'Item ID',
  `type` enum('spoken','subtitled') NOT NULL COMMENT 'Spoken or subtitled',
  `iso` varchar(16) NOT NULL COMMENT 'ISO language code',
  PRIMARY KEY (`iid`,`type`,`iso`),
  KEY `iso` (`iso`),
  CONSTRAINT `has_languages_ibfk_1` FOREIGN KEY (`iid`) REFERENCES `items` (`iid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `has_languages_ibfk_2` FOREIGN KEY (`iso`) REFERENCES `languages` (`iso`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8""")
HasLanguage = hasLanguagesTable.genClass()
HasLanguage.type_spoken = 'spoken'
HasLanguage.type_subtitled = 'subtitled'

def languageForceType(languages, type):
	"""
	Force all languages to be of the given type. Works with non-typed languages too.
	"""
	newLanguages = []
	for l in languages:
		if type(l) is type({}):
			newLanguages.append({
				'iso': l['iso'],
				'type': type
			})
		else:
			newLanguages.append({
				'iso': l,
				'type': type
			})
	return newLanguages

def languageAssumeType(languages, type):
	"""
	Same as languageForceType but don't change type of already-typed languages
	"""
	newLanguages = []
	for l in languages:
		if type(l) is type({}):
			newLanguages.append(l.copy())
		else:
			newLanguages.append({
				'iso': l,
				'type': type
			})
	return newLanguages

if __name__ == '__main__':
	# Sample data
	Language.create(iso='ab', english=u'Abkhaz', translated=u'аҧсуа бызшәа, аҧсшәа')
	Language.create(iso='aa', english=u'Afar', translated=u'Afaraf')
	Language.create(iso='af', english=u'Afrikaans', translated=u'Afrikaans')
	Language.create(iso='ak', english=u'Akan', translated=u'Akan')
	Language.create(iso='sq', english=u'Albanian', translated=u'gjuha shqipe')
	Language.create(iso='gsw', english=u'Alsatian', translated=u'Schwyzerdütsch, Elsassisch, Alemannisch')
	Language.create(iso='an', english=u'Aragonese', translated=u'aragonés')
	Language.create(iso='hy', english=u'Armenian', translated=u'Հայերեն')
	Language.create(iso='as', english=u'Assamese', translated=u'অসমীয়া')
	Language.create(iso='av', english=u'Avaric', translated=u'авар мацӀ, магӀарул мацӀ')
	Language.create(iso='ae', english=u'Avestan', translated=u'avesta')
	Language.create(iso='ay', english=u'Aymara', translated=u'aymar aru')
	Language.create(iso='az', english=u'Azerbaijani', translated=u'azərbaycan dili')
	Language.create(iso='bm', english=u'Bambara', translated=u'bamanankan')
	Language.create(iso='ba', english=u'Bashkir', translated=u'башҡорт теле')
	Language.create(iso='eu', english=u'Basque', translated=u'euskara, euskera')
	Language.create(iso='be', english=u'Belarusian', translated=u'беларуская мова')
	Language.create(iso='bn', english=u'Bengali', translated=u'বাংলা')
	Language.create(iso='bh', english=u'Bihari', translated=u'भोजपुरी')
	Language.create(iso='bi', english=u'Bislama', translated=u'Bislama')
	Language.create(iso='bjn', english=u'Banjar', translated=u'Bahasa Banjar')
	Language.create(iso='bs', english=u'Bosnian', translated=u'bosanski jezik')
	Language.create(iso='br', english=u'Breton', translated=u'brezhoneg')
	Language.create(iso='bg', english=u'Bulgarian', translated=u'български език')
	Language.create(iso='ch', english=u'Chamorro', translated=u'Chamoru')
	Language.create(iso='ce', english=u'Chechen', translated=u'нохчийн мотт')
	Language.create(iso='cv', english=u'Chuvash', translated=u'чӑваш чӗлхи')
	Language.create(iso='kw', english=u'Cornish', translated=u'Kernewek')
	Language.create(iso='co', english=u'Corsican', translated=u'corsu, lingua corsa')
	Language.create(iso='cr', english=u'Cree', translated=u'ᓀᐦᐃᔭᐍᐏᐣ')
	Language.create(iso='hr', english=u'Croatian', translated=u'hrvatski jezik')
	Language.create(iso='cs', english=u'Czech', translated=u'čeština, český jazyk')
	Language.create(iso='da', english=u'Danish', translated=u'dansk')
	Language.create(iso='day', english=u'Dayak', translated=u'Behas Dayak')
	Language.create(iso='nl', english=u'Dutch', translated=u'Nederlands, Vlaams')
	Language.create(iso='en', english=u'English', translated=u'English')
	Language.create(iso='eo', english=u'Esperanto', translated=u'Esperanto')
	Language.create(iso='et', english=u'Estonian', translated=u'eesti, eesti keel')
	Language.create(iso='ee', english=u'Ewe', translated=u'Eʋegbe')
	Language.create(iso='fo', english=u'Faroese', translated=u'føroyskt')
	Language.create(iso='fj', english=u'Fijian', translated=u'vosa Vakaviti')
	Language.create(iso='fi', english=u'Finnish', translated=u'suomi, suomen kieli')
	Language.create(iso='fr', english=u'French', translated=u'français, langue française')
	Language.create(iso='gl', english=u'Galician', translated=u'galego')
	Language.create(iso='ka', english=u'Georgian', translated=u'ქართული')
	Language.create(iso='de', english=u'German', translated=u'Deutsch')
	Language.create(iso='gu', english=u'Gujarati', translated=u'ગુજરાતી')
	Language.create(iso='hz', english=u'Herero', translated=u'Otjiherero')
	Language.create(iso='hi', english=u'Hindi', translated=u'हिन्दी, हिंदी')
	Language.create(iso='ho', english=u'Hiri Motu', translated=u'Hiri Motu')
	Language.create(iso='hu', english=u'Hungarian', translated=u'Magyar')
	Language.create(iso='ia', english=u'Interlingua', translated=u'Interlingua')
	Language.create(iso='id', english=u'Indonesian', translated=u'Bahasa Indonesia')
	Language.create(iso='ga', english=u'Irish', translated=u'Gaeilge')
	Language.create(iso='ig', english=u'Igbo', translated=u'Asụsụ Igbo')
	Language.create(iso='ik', english=u'Inupiaq', translated=u'Iñupiaq, Iñupiatun')
	Language.create(iso='io', english=u'Ido', translated=u'Ido')
	Language.create(iso='is', english=u'Icelandic', translated=u'Íslenska')
	Language.create(iso='it', english=u'Italian', translated=u'italiano')
	Language.create(iso='iu', english=u'Inuktitut', translated=u'ᐃᓄᒃᑎᑐᑦ')
	Language.create(iso='kn', english=u'Kannada', translated=u'ಕನ್ನಡ')
	Language.create(iso='kr', english=u'Kanuri', translated=u'Kanuri')
	Language.create(iso='kk', english=u'Kazakh', translated=u'қазақ тілі')
	Language.create(iso='km', english=u'Khmer', translated=u'ខ្មែរ, ខេមរភាសា, ភាសាខ្មែរ')
	Language.create(iso='rw', english=u'Kinyarwanda', translated=u'Ikinyarwanda')
	Language.create(iso='ky', english=u'Kyrgyz language', translated=u'[Кыргызча, Кыргыз тили]')
	Language.create(iso='kv', english=u'Komi', translated=u'коми кыв')
	Language.create(iso='kg', english=u'Kongo', translated=u'KiKongo')
	Language.create(iso='la', english=u'Latin', translated=u'latine, lingua latina')
	Language.create(iso='lg', english=u'Ganda', translated=u'Luganda')
	Language.create(iso='ln', english=u'Lingala', translated=u'Lingála')
	Language.create(iso='lo', english=u'Lao', translated=u'ພາສາລາວ')
	Language.create(iso='lt', english=u'Lithuanian', translated=u'lietuvių kalba')
	Language.create(iso='lv', english=u'Latvian', translated=u'latviešu valoda')
	Language.create(iso='gv', english=u'Manx', translated=u'Gaelg, Gailck')
	Language.create(iso='mk', english=u'Macedonian', translated=u'македонски јазик')
	Language.create(iso='mg', english=u'Malagasy', translated=u'Malagasy fiteny')
	Language.create(iso='ml', english=u'Malayalam', translated=u'മലയാളം')
	Language.create(iso='mt', english=u'Maltese', translated=u'Malti')
	Language.create(iso='mi', english=u'Māori', translated=u'te reo Māori')
	Language.create(iso='mr', english=u'Marathi (Marāṭhī)', translated=u'मराठी')
	Language.create(iso='mh', english=u'Marshallese', translated=u'Kajin M̧ajeļ')
	Language.create(iso='mn', english=u'Mongolian', translated=u'монгол')
	Language.create(iso='na', english=u'Nauru', translated=u'Ekakairũ Naoero')
	Language.create(iso='nb', english=u'Norwegian Bokmål', translated=u'Norsk bokmål')
	Language.create(iso='nd', english=u'North Ndebele', translated=u'isiNdebele')
	Language.create(iso='ne', english=u'Nepali', translated=u'नेपाली')
	Language.create(iso='ng', english=u'Ndonga', translated=u'Owambo')
	Language.create(iso='nn', english=u'Norwegian Nynorsk', translated=u'Norsk nynorsk')
	Language.create(iso='no', english=u'Norwegian', translated=u'Norsk')
	Language.create(iso='ii', english=u'Nuosu', translated=u'ꆈꌠ꒿ Nuosuhxop')
	Language.create(iso='nr', english=u'South Ndebele', translated=u'isiNdebele')
	Language.create(iso='om', english=u'Oromo', translated=u'Afaan Oromoo')
	Language.create(iso='or', english=u'Oriya', translated=u'ଓଡ଼ିଆ')
	Language.create(iso='pi', english=u'Pāli', translated=u'पाऴि')
	Language.create(iso='pt', english=u'Portuguese', translated=u'português')
	Language.create(iso='qu', english=u'Quechua', translated=u'Runa Simi, Kichwa')
	Language.create(iso='rm', english=u'Romansh', translated=u'rumantsch grischun')
	Language.create(iso='rn', english=u'Kirundi', translated=u'Ikirundi')
	Language.create(iso='ru', english=u'Russian', translated=u'русский язык')
	Language.create(iso='sa', english=u'Sanskrit (Saṁskṛta)', translated=u'संस्कृतम्')
	Language.create(iso='sc', english=u'Sardinian', translated=u'sardu')
	Language.create(iso='se', english=u'Northern Sami', translated=u'Davvisámegiella')
	Language.create(iso='sg', english=u'Sango', translated=u'yângâ tî sängö')
	Language.create(iso='sr', english=u'Serbian', translated=u'српски језик')
	Language.create(iso='sn', english=u'Shona', translated=u'chiShona')
	Language.create(iso='sk', english=u'Slovak', translated=u'slovenčina, slovenský jazyk')
	Language.create(iso='sl', english=u'Slovene', translated=u'slovenski jezik, slovenščina')
	Language.create(iso='so', english=u'Somali', translated=u'Soomaaliga, af Soomaali')
	Language.create(iso='st', english=u'Southern Sotho', translated=u'Sesotho')
	Language.create(iso='su', english=u'Sundanese', translated=u'Basa Sunda')
	Language.create(iso='sw', english=u'Swahili', translated=u'Kiswahili')
	Language.create(iso='ss', english=u'Swati', translated=u'SiSwati')
	Language.create(iso='sv', english=u'Swedish', translated=u'Svenska')
	Language.create(iso='ta', english=u'Tamil', translated=u'தமிழ்')
	Language.create(iso='te', english=u'Telugu', translated=u'తెలుగు')
	Language.create(iso='th', english=u'Thai', translated=u'ไทย')
	Language.create(iso='ti', english=u'Tigrinya', translated=u'ትግርኛ')
	Language.create(iso='tk', english=u'Turkmen', translated=u'Türkmen, Түркмен')
	Language.create(iso='tl', english=u'Tagalog', translated=u'Wikang Tagalog, ᜏᜒᜃᜅ᜔ ᜆᜄᜎᜓᜄ᜔')
	Language.create(iso='tn', english=u'Tswana', translated=u'Setswana')
	Language.create(iso='tr', english=u'Turkish', translated=u'Türkçe')
	Language.create(iso='ts', english=u'Tsonga', translated=u'Xitsonga')
	Language.create(iso='tw', english=u'Twi', translated=u'Twi')
	Language.create(iso='ty', english=u'Tahitian', translated=u'Reo Tahiti')
	Language.create(iso='ua', english=u'Ukrainian', translated=u'українська мова')
	Language.create(iso='ve', english=u'Venda', translated=u'Tshivenḓa')
	Language.create(iso='vi', english=u'Vietnamese', translated=u'Tiếng Việt')
	Language.create(iso='vo', english=u'Volapük', translated=u'Volapük')
	Language.create(iso='wa', english=u'Walloon', translated=u'walon')
	Language.create(iso='cy', english=u'Welsh', translated=u'Cymraeg')
	Language.create(iso='wo', english=u'Wolof', translated=u'Wollof')
	Language.create(iso='fy', english=u'Western Frisian', translated=u'Frysk')
	Language.create(iso='xh', english=u'Xhosa', translated=u'isiXhosa')
	Language.create(iso='yo', english=u'Yoruba', translated=u'Yorùbá')
	Language.create(iso='zu', english=u'Zulu', translated=u'isiZulu')
