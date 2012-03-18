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

echo Executing xquery example 1

XQUERY <titles> { for $t in db2-fn:xmlcolumn('BOOKS.TOC')/toc/chapter/chapter/chapter return <title> { data($t/@name) } </title> } </titles>

echo Executing xquery example 2

XQUERY <chapterlist> { for $c in db2-fn:xmlcolumn('BOOKS.TOC')/toc//chapter where fn:count($c//*) > 5 return <bigchapter subchapters="{ fn:count($c//*) }"> { $c } </bigchapter> } </chapterlist>
