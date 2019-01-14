import os,csv

a=str(2)
run1=os.system('python P2_P2.py '+a)
if run1==0:
    run2=os.system('python P1_P2.py')
    if run2==0:
        os.chdir('D:/Python/Data_Analysis/venv/History')
        with open('list.txt','r') as flist:
            for filename in flist:
                header_saved = False
                filefile='final_' + filename.replace('\n','')
                with open(filefile, 'w') as fout:
                    writer = csv.writer(fout)
                    with open(filename.replace('\n','')) as fin:
                        header = next(fin)
                        if not header_saved:
                            writer.writerows(header)  # you may need to work here. The writerows require an iterable.
                            header_saved = True
                        writer.writerows(fin.readlines())