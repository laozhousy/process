# #Available Functions
# TP.string_to_preprocessed_string()
# TP.string_to_sentence_tokenized_string_list()
# TP.string_to_preprocessed_sentence_tokenized_string_list()
# TP.string_to_word_tokenized_string_list()
# TP.string_to_preprocessed_word_tokenized_string_list()
# TP.sentence_tokenized_string_list_to_preprocessed_word_tokenized_string_list()
# TP.sentence_tokenized_string_list_to_word_tokenized_string_list()
# TP.sentence_tokenized_string_list_to_string()
# TP.sentence_tokenized_string_list_to_preprocessed_sentence_tokenized_string_list()
# TP.sentence_tokenized_string_list_to_preprocessed_string()
# TP.word_tokenized_string_list_to_preprocessed_word_tokenized_string_list()
# TP.word_tokenized_string_list_to_sentence_tokenized_string_list()
# TP.word_tokenized_string_list_to_preprocesed_sentence_tokenized_string_list()
# TP.word_tokenized_string_list_to_string()
# TP.word_tokenized_string_list_to_preprocessed_string()
#
# #Or Single Operations
# TP.lower_turkish()
# TP.lower_text()
# TP.remove_digits()
# TP.remove_link()
# TP.remove_punc()
# TP.stem_word()
# TP.remove_short_words()
# TP.remove_stop_words()
# TP.stem_string()
# TP.tokenize_word()
# TP.tokenize_sentence()
# TP.remove_blank() # Converts multiple spaces into single space.

# from TextPreprocesser import TextPreprocesser
#
# # train_text ="It was obvious from the very beginning he always regarded himself as a maverick, 555which the PM’s letter also suggest… https://t.co/RIVYzNePq1"
# #             #"https://t.co/T30YSJFz2v"
# # TP = TextPreprocesser(lang="english", lower=True, digits=True, link=True, punc=True,
# #                  stem=False, stop_words=False, min_length_count=0)
# # print(TP.stem_word(train_text))
# # result = TP.string_to_preprocessed_string(train_text)
# #
# # print(result)
# #
# #
# # TP3 = TextPreprocesser(lang="english", lower=True, digits=True, link=True, punc=True,
# #                  stem=False, stop_words=True, min_length_count=0)
# # test3 = "It was obvious from the very beginning he always regarded himself as a maverick, which the PM’s letter also suggest… https://t.co/T30YSJFz2v"
# #
# # result3 = TP3.string_to_preprocessed_string(test3)
# #
# # print(result3)
# # # i am not an athenian or a greek  but a citizen of the world   diogenes
# #
# #
# #
# TP2 = TextPreprocesser(lang="english", lower=True, digits=False, link=True, punc=False,
#                  stem=False, stop_words=True, min_length_count=0)
# test2 = "It was obvious from the very beginning he always regarded himself as a maverick, 🐯💛5555which the PM’s letter also suggest… https://t.co/T30YSJFz2v"
# result2 = TP2.string_to_preprocessed_string(test2)
# result2 = TP2.remove_digits(result2)
# result2 = TP2.remove_blank(result2)
# print(result2)
#
#
# train_text ="RT @sohmer: @realDonaldTrump The Importer pays the tariffs, you fucking moron. You’ve levied a sales tax on yours own citizens."
# TP = TextPreprocesser(lang="english", lower=True, digits=False, link=True, punc=False,
#                  stem=False, stop_words=True, min_length_count=0)
# result = TP.string_to_preprocessed_string(train_text)
# result = TP.remove_digits(result)
# result = TP.remove_blank(result)
# print(result)

import pandas as pd
# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
# pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 10240)#加了这一行那表格的一行就不会分段出现了
# pd.set_option('display.max_colwidth', 1000)
# pd.set_option('display.height', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',500)

# train=pd.read_csv("../data/Constraint/handi/constraint_Hindi_Train - Sheet1.csv")
valid=pd.read_csv("../data/Constraint/handi/constraint_Hindi_train - Sheet1.csv")
valid.columns = ['id','post','label']
print(valid.count())
# print(train.id.value_counts())
# print(train.post.value_counts())
print(valid.label.value_counts())
# print(train['label'])

valid['defamation'] = 0
valid['fake'] = 0
valid['hate'] = 0
valid['offensive'] = 0
valid['non-hostile'] = 0

print(type(valid['hate']))
# for i,row in valid.iterrows():
#     if(row['label'] == "non-hostile"):#435
#         valid.loc[i,'non-hostile'] = 1
#     if (row['label'] == "fake"):#144
#         valid.loc[i, 'fake'] = 1
#     if (row['label'] == "hate"):#68
#         valid.loc[i, 'hate'] = 1
#     if (row['label'] == "offensive"):#57
#         valid.loc[i, 'offensive'] = 1
#     if (row['label'] == "defamation"):#43
#         valid.loc[i, 'defamation'] = 1
#     if (row['label'] == "hate,offensive"):#23
#         valid.loc[i, 'hate'] = 1
#         valid.loc[i, 'offensive'] = 1
#     if (row['label'] == "defamation,offensive"):#11
#         valid.loc[i, 'defamation'] = 1
#         valid.loc[i, 'offensive'] = 1
#     if (row['label'] == "defamation,hate"):#10
#         valid.loc[i, 'defamation'] = 1
#         valid.loc[i, 'hate'] = 1
#     if (row['label'] == "fake,offensive"):#4
#         valid.loc[i, 'fake'] = 1
#         valid.loc[i, 'offensive'] = 1
#     if (row['label'] == "defamation,hate,offensive"):#4
#         valid.loc[i, 'defamation'] = 1
#         valid.loc[i, 'hate'] = 1
#         valid.loc[i, 'offensive'] = 1
#     if (row['label'] == "defamation,fake"):#4
#         valid.loc[i, 'defamation'] = 1
#         valid.loc[i, 'fake'] = 1
#     if (row['label'] == "fake,hate"):#3
#         valid.loc[i, 'fake'] = 1
#         valid.loc[i, 'hate'] = 1
#     if (row['label'] == "defamation,fake,offensive"):#3
#         valid.loc[i, 'defamation'] = 1
#         valid.loc[i, 'fake'] = 1
#         valid.loc[i, 'offensive'] = 1
#     if (row['label'] == "defamation,fake,hate"):#1
#         valid.loc[i, 'defamation'] = 1
#         valid.loc[i, 'fake'] = 1
#         valid.loc[i, 'hate'] = 1
#     if (row['label'] == "defamation,fake,hate,offensive"):#1
#         valid.loc[i, 'defamation'] = 1
#         valid.loc[i, 'fake'] = 1
#         valid.loc[i, 'hate'] = 1
#         valid.loc[i, 'offensive'] = 1
#
#
#
#
# #以下保存指定的列到新的csv文件，index=0表示不为每一行自动编号，header=1表示行首有字段名称
# valid.to_csv('handi_valid_preprocessing.csv',columns=['id','post','label','defamation','fake','hate','offensive','non-hostile'],index=0,header=1)
#














# print(train)
# print('\n\n')
# from TextPreprocesser import TextPreprocesser
# TP = TextPreprocesser(lang="english", lower=True, digits=False, link=True, punc=False,
#                  stem=True, stop_words=True, min_length_count=2)
# train_text = 'hate wen females hit ah nigga with tht bro 😂😂, I’m tryna make u my la sweety , fuck ah bro'
# # train_text = '@canelo28969897 @ItsCandyyyyyyy @DiamondRhona @darrel30901325 @Noblenosey Don’t nobody want no damn white man ew &amp;… https://t.co/cuzxJAzFGL'
# # train_text = 'RT @YoungTheGoat: Nigga Said “Wyd” niggas are sick 😭😂 https://t.co/pdXY24sSHn'
# result = TP.string_to_preprocessed_string(train_text)
# result = TP.remove_digits(result)
# result = TP.remove_blank(result)
# print(result)

# print(train.loc[:,['text']])
# print('\n\n')

# print(train.loc[0,['text']])
#

# s = pd.Series(s,dtype='str')
# s.astype('str')
# print(s)


# from TextPreprocesser import TextPreprocesser
# TP = TextPreprocesser(lang="english", lower=True, digits=False, link=True, punc=False,
#                  stem=True, stop_words=True, min_length_count=2)
#
#
# for i in train['text'].index:
#     s = train.loc[i,'text']
#     # print(type(s))
#     #print(s)
#     s = TP.string_to_preprocessed_string(s)
#     s = TP.remove_digits(s)
#     s = TP.remove_blank(s)
#     train.loc[i, 'text'] = s
#     # print(s)
#
# train.loc[train['task1'] =='NOT','task1']= 0
# train.loc[train['task1'] =='HOF','task1']= 1
#
# train.loc[train['task2'] =='NONE','task2']= 0
# train.loc[train['task2'] =='PRFN','task2']= 1
# train.loc[train['task2'] =='OFFN','task2']= 2
# train.loc[train['task2'] =='HATE','task2']= 3
#
#
# print(train)
#
# train.to_csv('handi_train_preprocessing.csv', index=0)

