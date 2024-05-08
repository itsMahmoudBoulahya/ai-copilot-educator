from rag import ChatPDF

model = ChatPDF()
model.ingests({"./pdf/oltest.pdf"})
for s in model.chain.stream("give me the text on the first chapter of the provided pdf file"):
  print(s,end='')
print()