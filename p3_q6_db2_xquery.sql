echo Creating schema...

DROP TABLE items

DROP TABLE books

CREATE TABLE items(iid int NOT NULL, title varchar(255) NOT NULL, date date NOT NULL, PRIMARY KEY (iid))

CREATE TABLE books(iid int NOT NULL, isbn bigint NOT NULL, pages int NOT NULL, toc XML, PRIMARY KEY(iid), FOREIGN KEY(iid) REFERENCES items(iid))

echo Inserting rows...

INSERT INTO items(iid, title, date) VALUES(1, 'Guide to writing', '2006-04-11')

INSERT INTO books(iid, isbn, pages, toc) VALUES(1, 1337, 32, '<toc><chapter num="1" title="INTRODUCTION" page="3"><chapter num="1.a" title="Style" page="3"/><chapter num="1.b" title="Composition and Structure" page="3"/><chapter num="1.c" title="Acknowledgement of Support" page="4"/><chapter num="1.d" title="Abstract" page="4"/></chapter><chapter num="2" title="MANUSCRIPT PREPARATION" page="4"><chapter num="2.a" title="Paper and Duplication" page="4"/><chapter num="2.b" title="Printing" page="4"/><chapter num="2.c" title="Font" page="4"/><chapter num="2.d" title="Margins" page="4"/><chapter num="2.e" title="Pagination" page="5"/><chapter num="2.f" title="Spacing" page="5"/><chapter num="2.g" title="Numbering Schemes" page="5"/><chapter num="2.h" title="Division" page="5"><chapter num="2.h.1" title="Body of Manuscript" page="5"/><chapter num="2.h.2" title="Words and Sentences" page="5"/><chapter num="2.h.3" title="Headings and Subheadings" page="6"/></chapter><chapter num="2.i" title="Tables and Figures" page="6"/><chapter num="2.j" title="Table of Contents Preparation Hint" page="6"/></chapter></toc>')

INSERT INTO items(iid, title, date) VALUES(2, 'Non-Natural Amino Acids', '2009-06-21')

INSERT INTO books(iid, isbn, pages, toc) VALUES(2, 9002, 262, '<toc><chapter num="1" name="Protein Phosphorylation by Semisynthesis: From Paper to Practice" page="1"><chapter num="1.1" name="Overview of Protein Phosphorylation" page="2"/><chapter num="1.2" name="Investigating Protein Phosphorylation with Phosphomemetics" page="3"/><chapter num="1.3" name="Phosphonates Analogues and Protein Semisynthesis" page="5"/><chapter num="1.4" name="Methods" page="6"/></chapter><chapter num="2" name="Protein Engineering with the Traceless Staudinger Ligation" page="25"><chapter num="2.1" name="Introduction" page="26"/><chapter num="2.2" name="Traceless Staudinger Legation" page="26"/><chapter num="2.3" name="Choice of Coupling Reagent" page="28"/><chapter num="2.4" name="Preparation of the Azido Fragment" page="33"/></chapter></toc>')