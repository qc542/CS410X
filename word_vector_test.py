from word_vector import *

entire_vector = load_vector("/Users/qilei/Downloads/wiki-news-300d-1M.vec")
# Path to vector file on macOS

#entire_vector = load_vector(r"C:\Users\qilei\Downloads\wiki-news-300d-1M.vec")
# Path to vector file on Windows

professions = ["professor", "boss", "student", "engineer", "doctor",
               "dentist", "manager", "journalist"]
venues = ["hospital", "pharmacy", "mall", "salon", "restaurant"]
professions_words = construct_word_list(professions, entire_vector)
venues_words = construct_word_list(venues, entire_vector)

print(sorted_by_similarity(professions_words, lookup_vector("surgeon",
                                                            entire_vector)))
