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

def languageForceType(languages, languageType):
	"""
	Force all languages to be of the given type. Works with non-typed languages too.
	"""
	newLanguages = []
	for l in languages:
		if type(l) is type({}):
			newLanguages.append({
				'iso': l['iso'],
				'type': languageType
			})
		else:
			newLanguages.append({
				'iso': l,
				'type': languageType
			})
	return newLanguages

def languageAssumeType(languages, languageType):
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
				'type': languageType
			})
	return newLanguages

# From Wikipedia: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
languageData = [
	{'iso': 'ab', 'english': u'Abkhaz', 'translated': u'аҧсуа бызшәа, аҧсшәа'},
	{'iso': 'aa', 'english': u'Afar', 'translated': u'Afaraf'},
	{'iso': 'af', 'english': u'Afrikaans', 'translated': u'Afrikaans'},
	{'iso': 'ak', 'english': u'Akan', 'translated': u'Akan'},
	{'iso': 'sq', 'english': u'Albanian', 'translated': u'gjuha shqipe'},
	{'iso': 'gsw', 'english': u'Alsatian', 'translated': u'Schwyzerdütsch, Elsassisch, Alemannisch'},
	{'iso': 'an', 'english': u'Aragonese', 'translated': u'aragonés'},
	{'iso': 'hy', 'english': u'Armenian', 'translated': u'Հայերեն'},
	{'iso': 'as', 'english': u'Assamese', 'translated': u'অসমীয়া'},
	{'iso': 'av', 'english': u'Avaric', 'translated': u'авар мацӀ, магӀарул мацӀ'},
	{'iso': 'ae', 'english': u'Avestan', 'translated': u'avesta'},
	{'iso': 'ay', 'english': u'Aymara', 'translated': u'aymar aru'},
	{'iso': 'az', 'english': u'Azerbaijani', 'translated': u'azərbaycan dili'},
	{'iso': 'bm', 'english': u'Bambara', 'translated': u'bamanankan'},
	{'iso': 'ba', 'english': u'Bashkir', 'translated': u'башҡорт теле'},
	{'iso': 'eu', 'english': u'Basque', 'translated': u'euskara, euskera'},
	{'iso': 'be', 'english': u'Belarusian', 'translated': u'беларуская мова'},
	{'iso': 'bn', 'english': u'Bengali', 'translated': u'বাংলা'},
	{'iso': 'bh', 'english': u'Bihari', 'translated': u'भोजपुरी'},
	{'iso': 'bi', 'english': u'Bislama', 'translated': u'Bislama'},
	{'iso': 'bjn', 'english': u'Banjar', 'translated': u'Bahasa Banjar'},
	{'iso': 'bs', 'english': u'Bosnian', 'translated': u'bosanski jezik'},
	{'iso': 'br', 'english': u'Breton', 'translated': u'brezhoneg'},
	{'iso': 'bg', 'english': u'Bulgarian', 'translated': u'български език'},
	{'iso': 'ch', 'english': u'Chamorro', 'translated': u'Chamoru'},
	{'iso': 'ce', 'english': u'Chechen', 'translated': u'нохчийн мотт'},
	{'iso': 'cv', 'english': u'Chuvash', 'translated': u'чӑваш чӗлхи'},
	{'iso': 'kw', 'english': u'Cornish', 'translated': u'Kernewek'},
	{'iso': 'co', 'english': u'Corsican', 'translated': u'corsu, lingua corsa'},
	{'iso': 'cr', 'english': u'Cree', 'translated': u'ᓀᐦᐃᔭᐍᐏᐣ'},
	{'iso': 'hr', 'english': u'Croatian', 'translated': u'hrvatski jezik'},
	{'iso': 'cs', 'english': u'Czech', 'translated': u'čeština, český jazyk'},
	{'iso': 'da', 'english': u'Danish', 'translated': u'dansk'},
	{'iso': 'day', 'english': u'Dayak', 'translated': u'Behas Dayak'},
	{'iso': 'nl', 'english': u'Dutch', 'translated': u'Nederlands, Vlaams'},
	{'iso': 'en', 'english': u'English', 'translated': u'English'},
	{'iso': 'eo', 'english': u'Esperanto', 'translated': u'Esperanto'},
	{'iso': 'et', 'english': u'Estonian', 'translated': u'eesti, eesti keel'},
	{'iso': 'ee', 'english': u'Ewe', 'translated': u'Eʋegbe'},
	{'iso': 'fo', 'english': u'Faroese', 'translated': u'føroyskt'},
	{'iso': 'fj', 'english': u'Fijian', 'translated': u'vosa Vakaviti'},
	{'iso': 'fi', 'english': u'Finnish', 'translated': u'suomi, suomen kieli'},
	{'iso': 'fr', 'english': u'French', 'translated': u'français, langue française'},
	{'iso': 'gl', 'english': u'Galician', 'translated': u'galego'},
	{'iso': 'ka', 'english': u'Georgian', 'translated': u'ქართული'},
	{'iso': 'de', 'english': u'German', 'translated': u'Deutsch'},
	{'iso': 'gu', 'english': u'Gujarati', 'translated': u'ગુજરાતી'},
	{'iso': 'hz', 'english': u'Herero', 'translated': u'Otjiherero'},
	{'iso': 'hi', 'english': u'Hindi', 'translated': u'हिन्दी, हिंदी'},
	{'iso': 'ho', 'english': u'Hiri Motu', 'translated': u'Hiri Motu'},
	{'iso': 'hu', 'english': u'Hungarian', 'translated': u'Magyar'},
	{'iso': 'ia', 'english': u'Interlingua', 'translated': u'Interlingua'},
	{'iso': 'id', 'english': u'Indonesian', 'translated': u'Bahasa Indonesia'},
	{'iso': 'ga', 'english': u'Irish', 'translated': u'Gaeilge'},
	{'iso': 'ig', 'english': u'Igbo', 'translated': u'Asụsụ Igbo'},
	{'iso': 'ik', 'english': u'Inupiaq', 'translated': u'Iñupiaq, Iñupiatun'},
	{'iso': 'io', 'english': u'Ido', 'translated': u'Ido'},
	{'iso': 'is', 'english': u'Icelandic', 'translated': u'Íslenska'},
	{'iso': 'it', 'english': u'Italian', 'translated': u'italiano'},
	{'iso': 'iu', 'english': u'Inuktitut', 'translated': u'ᐃᓄᒃᑎᑐᑦ'},
	{'iso': 'kn', 'english': u'Kannada', 'translated': u'ಕನ್ನಡ'},
	{'iso': 'kr', 'english': u'Kanuri', 'translated': u'Kanuri'},
	{'iso': 'kk', 'english': u'Kazakh', 'translated': u'қазақ тілі'},
	{'iso': 'km', 'english': u'Khmer', 'translated': u'ខ្មែរ, ខេមរភាសា, ភាសាខ្មែរ'},
	{'iso': 'rw', 'english': u'Kinyarwanda', 'translated': u'Ikinyarwanda'},
	{'iso': 'ky', 'english': u'Kyrgyz language', 'translated': u'[Кыргызча, Кыргыз тили]'},
	{'iso': 'kv', 'english': u'Komi', 'translated': u'коми кыв'},
	{'iso': 'kg', 'english': u'Kongo', 'translated': u'KiKongo'},
	{'iso': 'la', 'english': u'Latin', 'translated': u'latine, lingua latina'},
	{'iso': 'lg', 'english': u'Ganda', 'translated': u'Luganda'},
	{'iso': 'ln', 'english': u'Lingala', 'translated': u'Lingála'},
	{'iso': 'lo', 'english': u'Lao', 'translated': u'ພາສາລາວ'},
	{'iso': 'lt', 'english': u'Lithuanian', 'translated': u'lietuvių kalba'},
	{'iso': 'lv', 'english': u'Latvian', 'translated': u'latviešu valoda'},
	{'iso': 'gv', 'english': u'Manx', 'translated': u'Gaelg, Gailck'},
	{'iso': 'mk', 'english': u'Macedonian', 'translated': u'македонски јазик'},
	{'iso': 'mg', 'english': u'Malagasy', 'translated': u'Malagasy fiteny'},
	{'iso': 'ml', 'english': u'Malayalam', 'translated': u'മലയാളം'},
	{'iso': 'mt', 'english': u'Maltese', 'translated': u'Malti'},
	{'iso': 'mi', 'english': u'Māori', 'translated': u'te reo Māori'},
	{'iso': 'mr', 'english': u'Marathi (Marāṭhī)', 'translated': u'मराठी'},
	{'iso': 'mh', 'english': u'Marshallese', 'translated': u'Kajin M̧ajeļ'},
	{'iso': 'mn', 'english': u'Mongolian', 'translated': u'монгол'},
	{'iso': 'na', 'english': u'Nauru', 'translated': u'Ekakairũ Naoero'},
	{'iso': 'nb', 'english': u'Norwegian Bokmål', 'translated': u'Norsk bokmål'},
	{'iso': 'nd', 'english': u'North Ndebele', 'translated': u'isiNdebele'},
	{'iso': 'ne', 'english': u'Nepali', 'translated': u'नेपाली'},
	{'iso': 'ng', 'english': u'Ndonga', 'translated': u'Owambo'},
	{'iso': 'nn', 'english': u'Norwegian Nynorsk', 'translated': u'Norsk nynorsk'},
	{'iso': 'no', 'english': u'Norwegian', 'translated': u'Norsk'},
	{'iso': 'ii', 'english': u'Nuosu', 'translated': u'ꆈꌠ꒿ Nuosuhxop'},
	{'iso': 'nr', 'english': u'South Ndebele', 'translated': u'isiNdebele'},
	{'iso': 'om', 'english': u'Oromo', 'translated': u'Afaan Oromoo'},
	{'iso': 'or', 'english': u'Oriya', 'translated': u'ଓଡ଼ିଆ'},
	{'iso': 'pi', 'english': u'Pāli', 'translated': u'पाऴि'},
	{'iso': 'pt', 'english': u'Portuguese', 'translated': u'português'},
	{'iso': 'qu', 'english': u'Quechua', 'translated': u'Runa Simi, Kichwa'},
	{'iso': 'rm', 'english': u'Romansh', 'translated': u'rumantsch grischun'},
	{'iso': 'rn', 'english': u'Kirundi', 'translated': u'Ikirundi'},
	{'iso': 'ru', 'english': u'Russian', 'translated': u'русский язык'},
	{'iso': 'sa', 'english': u'Sanskrit (Saṁskṛta)', 'translated': u'संस्कृतम्'},
	{'iso': 'sc', 'english': u'Sardinian', 'translated': u'sardu'},
	{'iso': 'se', 'english': u'Northern Sami', 'translated': u'Davvisámegiella'},
	{'iso': 'sg', 'english': u'Sango', 'translated': u'yângâ tî sängö'},
	{'iso': 'sr', 'english': u'Serbian', 'translated': u'српски језик'},
	{'iso': 'sn', 'english': u'Shona', 'translated': u'chiShona'},
	{'iso': 'sk', 'english': u'Slovak', 'translated': u'slovenčina, slovenský jazyk'},
	{'iso': 'sl', 'english': u'Slovene', 'translated': u'slovenski jezik, slovenščina'},
	{'iso': 'so', 'english': u'Somali', 'translated': u'Soomaaliga, af Soomaali'},
	{'iso': 'st', 'english': u'Southern Sotho', 'translated': u'Sesotho'},
	{'iso': 'su', 'english': u'Sundanese', 'translated': u'Basa Sunda'},
	{'iso': 'sw', 'english': u'Swahili', 'translated': u'Kiswahili'},
	{'iso': 'ss', 'english': u'Swati', 'translated': u'SiSwati'},
	{'iso': 'sv', 'english': u'Swedish', 'translated': u'Svenska'},
	{'iso': 'ta', 'english': u'Tamil', 'translated': u'தமிழ்'},
	{'iso': 'te', 'english': u'Telugu', 'translated': u'తెలుగు'},
	{'iso': 'th', 'english': u'Thai', 'translated': u'ไทย'},
	{'iso': 'ti', 'english': u'Tigrinya', 'translated': u'ትግርኛ'},
	{'iso': 'tk', 'english': u'Turkmen', 'translated': u'Türkmen, Түркмен'},
	{'iso': 'tl', 'english': u'Tagalog', 'translated': u'Wikang Tagalog, ᜏᜒᜃᜅ᜔ ᜆᜄᜎᜓᜄ᜔'},
	{'iso': 'tn', 'english': u'Tswana', 'translated': u'Setswana'},
	{'iso': 'tr', 'english': u'Turkish', 'translated': u'Türkçe'},
	{'iso': 'ts', 'english': u'Tsonga', 'translated': u'Xitsonga'},
	{'iso': 'tw', 'english': u'Twi', 'translated': u'Twi'},
	{'iso': 'ty', 'english': u'Tahitian', 'translated': u'Reo Tahiti'},
	{'iso': 'ua', 'english': u'Ukrainian', 'translated': u'українська мова'},
	{'iso': 've', 'english': u'Venda', 'translated': u'Tshivenḓa'},
	{'iso': 'vi', 'english': u'Vietnamese', 'translated': u'Tiếng Việt'},
	{'iso': 'vo', 'english': u'Volapük', 'translated': u'Volapük'},
	{'iso': 'wa', 'english': u'Walloon', 'translated': u'walon'},
	{'iso': 'cy', 'english': u'Welsh', 'translated': u'Cymraeg'},
	{'iso': 'wo', 'english': u'Wolof', 'translated': u'Wollof'},
	{'iso': 'fy', 'english': u'Western Frisian', 'translated': u'Frysk'},
	{'iso': 'xh', 'english': u'Xhosa', 'translated': u'isiXhosa'},
	{'iso': 'yo', 'english': u'Yoruba', 'translated': u'Yorùbá'},
	{'iso': 'zu', 'english': u'Zulu', 'translated': u'isiZulu'}
]

def createLanguageData():
	for l in languageData:
		Language.create(**l)
