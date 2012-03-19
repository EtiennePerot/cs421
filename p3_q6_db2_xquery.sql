connect to cs421

echo Creating schema...

DROP TABLE items

DROP TABLE books

CREATE TABLE items(iid int NOT NULL, title varchar(255) NOT NULL, date date NOT NULL, PRIMARY KEY (iid))

CREATE TABLE books(iid int NOT NULL, isbn bigint NOT NULL, pages int NOT NULL, toc XML, PRIMARY KEY(iid), FOREIGN KEY(iid) REFERENCES items(iid))

echo Inserting rows...

INSERT INTO items(iid, title, date) VALUES(1, 'Guide to writing', '2006-04-11')

INSERT INTO books(iid, isbn, pages, toc) VALUES(1, 1337, 32, '<toc><chapter num="1" name="INTRODUCTION" page="3"><chapter num="1.a" name="Style" page="3"/><chapter num="1.b" name="Composition and Structure" page="3"/><chapter num="1.c" name="Acknowledgement of Support" page="4"/><chapter num="1.d" name="Abstract" page="4"/></chapter><chapter num="2" name="MANUSCRIPT PREPARATION" page="4"><chapter num="2.a" name="Paper and Duplication" page="4"/><chapter num="2.b" name="Printing" page="4"/><chapter num="2.c" name="Font" page="4"/><chapter num="2.d" name="Margins" page="4"/><chapter num="2.e" name="Pagination" page="5"/><chapter num="2.f" name="Spacing" page="5"/><chapter num="2.g" name="Numbering Schemes" page="5"/><chapter num="2.h" name="Division" page="5"><chapter num="2.h.1" name="Body of Manuscript" page="5"/><chapter num="2.h.2" name="Words and Sentences" page="5"/><chapter num="2.h.3" name="Headings and Subheadings" page="6"/></chapter><chapter num="2.i" name="Tables and Figures" page="6"/><chapter num="2.j" name="Table of Contents Preparation Hint" page="6"/></chapter></toc>')

INSERT INTO items(iid, title, date) VALUES(2, 'Non-Natural Amino Acids', '2009-06-21')

INSERT INTO books(iid, isbn, pages, toc) VALUES(2, 9002, 262, '<toc><chapter num="1" name="Protein Phosphorylation by Semisynthesis: From Paper to Practice" page="1"><chapter num="1.1" name="Overview of Protein Phosphorylation" page="2"/><chapter num="1.2" name="Investigating Protein Phosphorylation with Phosphomemetics" page="3"/><chapter num="1.3" name="Phosphonates Analogues and Protein Semisynthesis" page="5"/><chapter num="1.4" name="Methods" page="6"/></chapter><chapter num="2" name="Protein Engineering with the Traceless Staudinger Ligation" page="25"><chapter num="2.1" name="Introduction" page="26"/><chapter num="2.2" name="Traceless Staudinger Legation" page="26"/><chapter num="2.3" name="Choice of Coupling Reagent" page="28"/><chapter num="2.4" name="Preparation of the Azido Fragment" page="33"/></chapter></toc>')

INSERT INTO items(iid, title, date) VALUES(3, 'Principles of Model Checking', '2008-02-07')

INSERT INTO books(iid, isbn, pages, toc) VALUES(3, 6542, 994, '<toc><chapter num="1" name="System Veriﬁcation" page="1"><chapter num="1.1" name="Model checking" page="7"/><chapter num="1.2" name="Characteristics of Model Checking" page="11"><chapter num="1.2.1" name="The Model-Checking Process" page="11"/><chapter num="1.2.2" name="Strengths and Weaknesses" page="14"/></chapter><chapter num="1.3" name="Bibliographic notes" page="16"/></chapter><chapter num="2" name="Modelling Concurrent Systems" page="19"><chapter num="2.1" name="Transition Systems" page="19"><chapter num="2.1.1" name="Executions" page="24"/><chapter num="2.1.2" name="Modeling Hardware and Software Systems" page="26"/></chapter><chapter num="2.2" name="Parallelism and Communication" page="35"><chapter num="2.2.1" name="Concurrency and Interleaving" page="36"/><chapter num="2.2.2" name="Communication via Shared Variables" page="39"/><chapter num="2.2.3" name="Handshaking" page="47"/><chapter num="2.2.4" name="Channel Systems" page="53"/><chapter num="2.2.5" name="NanoPromela" page="63"/><chapter num="2.2.6" name="Synchronous Parallelism" page="75"/></chapter><chapter num="2.3" name="The State-Space Explosion Problem" page="77"/><chapter num="2.4" name="Summary" page="80"/><chapter num="2.5" name="Bibliographic Notes" page="80"/><chapter num="2.6" name="Exercises" page="82"/></chapter></toc>')

INSERT INTO items(iid, title, date) VALUES(4, 'Algorithm Design', '2009-02-20')

INSERT INTO books(iid, isbn, pages, toc) VALUES(4, 879451, 432, '<toc><chapter num="I" name="Introduction: Some Representative Problems" page="1"><chapter num="I.1" name="A First Problem: Stable Matching" page="12"/><chapter num="I.2" name="Five Representative Problems" page="19"/><chapter num="I.3" name="Solved Exercises" page="22"/><chapter num="I.4" name="Notes and Further Reading" page="28"/></chapter><chapter num="II" name="Basics of Algorithm Analysis" page="29"><chapter num="II.1" name="Computational Tractability" page="29"/><chapter num="II.2" name="Asymptotic Order of Growth" page="35"/><chapter num="II.3" name="Implementing the Stable Matching Algorithm Using Lists and Arrays" page="42"/><chapter num="II.4" name="A Survey of Common Running Times" page="47"/><chapter num="II.5" name="A More Complex Data Structure: Priority Queues" page="57"/><chapter num="II.6" name="Solved Exercises" page="65"/><chapter num="II.7" name="Exercises" page="67"/><chapter num="II.8" name="Notes and Further Reading" page="70"/></chapter></toc>')

INSERT INTO items(iid, title, date) VALUES(10002, 'The Binding of Matheus', '2004-03-28')

INSERT INTO books(iid, isbn, pages, toc) VALUES(10002, 8999, 150, '<toc><chapter num="1" name="The Binding of Matheus" page="1"><chapter num="1.1" name="The Revelation" page="2"/><chapter num="1.2" name="Escape to the Abyss" page="20"/><chapter num="1.3" name="The Iron Gate" page="36"/><chapter num="1.4" name="Keeper of the key" page="42"/><chapter num="1.5" name="Unfriendly Encounter" page="57"/></chapter><chapter num="2" name="The Sword of Nexus" page="68"><chapter num="2.1" name="The Order of Kalimdor" page="69"/><chapter num="2.2" name="The Conquest of Isaroth" page="86"/><chapter num="2.3" name="The Nexus" page="100"/></chapter><chapter num="3" name="The Apocalypse" page="108"><chapter num="3.1" name="The Rift " page="109"/><chapter num="3.2" name="Mirror World" page="119"/><chapter num="3.3" name="The Final Encounter" page="132"/><chapter num="3.4" name="To Kalimdor" page="145"/></chapter></toc>')

INSERT INTO items(iid, title, date) VALUES(5023, 'Cooking for dummies', '2005-02-01')

INSERT INTO books(iid, isbn, pages, to) VALUES(5023, 8999, 17, '<toc><chapter num="1" name="Entrees" page="1"><chapter num="1.1" name="Grilled chicken" page="2"/><chapter num="1.2" name="Braised duck" page="3"/><chapter num="1.3" name="Chicken noodles" page="4"/><chapter num="1.4" name="Sushi" page="5"/><chapter num="1.5" name="Fried fish" page="6"/></chapter><chapter num="2" name="Main dishes" page="7"><chapter num="2.1" name="Pork chop" page="8"/><chapter num="2.2" name="5 cheese pizza " page="9"/><chapter num="2.3" name="Pineapple salad" page="10"/></chapter><chapter num="3" name="Desserts" page="11"><chapter num="3.1" name="Soufflé" page="12"/><chapter num="3.2" name="Yogurt cake" page="13"/><chapter num="3.3" name="Fruit salad" page="14"/><chapter num="3.4" name="Baklava" page="15"/></chapter></toc>')

INSERT INTO items(iid, title, date) VALUES(8769, 'Python 101', '2010-12-08')

INSERT INTO books(iid, isbn, pages, to) VALUES(8769, 3923, 46, '<toc><chapter num="1" page="1"><chapter num="1.1" name="Introduction" page="2"/><chapter num="1.2" name="Main features" page="5"/><chapter num="1.3" name="Interactive Python" page="10"/><chapter num="1.4" name="Data types" page="13"/><chapter num="1.5" name="Simple statements" page="16"/></chapter><chapter num="1.6" name="Control structures" page="20"/><chapter num="1.7" name="Organization " page="24"/><chapter num="1.7" name="Main libraries" page="30"/></chapter><chapter num="1.8" name="Serialization" page="34"><chapter num="1.9" name="Unit testing" page="36"/><chapter num="1.10" name="Conclusion" page="42"/></chapter></toc>')


echo Executing xquery example 1

XQUERY <titles> { for $t in db2-fn:xmlcolumn('BOOKS.TOC')/toc/chapter/chapter/chapter return <title> { data($t/@name) } </title> } </titles>

echo Executing xquery example 2

XQUERY <chapterlist> { for $c in db2-fn:xmlcolumn('BOOKS.TOC')/toc//chapter where fn:count($c//*) > 5 return <bigchapter subchapters="{ fn:count($c//*) }"> { $c } </bigchapter> } </chapterlist>
