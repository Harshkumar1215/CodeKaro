# -*- coding: utf-8 -*-
import json
import sys

# Ensure UTF-8 output on Windows console
sys.stdout.reconfigure(encoding='utf-8')

def verify():
    with open('js/data/syllabus.js', 'r', encoding='utf-8') as f:
        text = f.read()

    prefix = 'window.BSEB_SYLLABUS = '
    start = text.find(prefix) + len(prefix)
    end = text.rfind(';')
    json_text = text[start:end].strip()

    data = json.loads(json_text)
    print("Board:", data['board'], "-", data['board_name_hi'], "/", data['board_name_en'])
    print("Class:", data['class'], "-", data['class_name_hi'], "/", data['class_name_en'])

    total_subs = len(data['subjects'])
    total_books = 0
    total_sections = 0
    total_chapters = 0
    total_topics = 0

    all_ids = set()

    for sub in data['subjects']:
        sub_id = sub['id']
        assert sub_id not in all_ids, f"Duplicate ID: {sub_id}"
        all_ids.add(sub_id)
        assert sub['name_hi'] and sub['name_en']
        total_books += len(sub['books'])
        print(f"\n[Subject]: {sub_id} | {sub['name_hi']} / {sub['name_en']}")

        for book in sub['books']:
            b_id = book['id']
            assert b_id not in all_ids, f"Duplicate ID: {b_id}"
            all_ids.add(b_id)
            assert book['name_hi'] and book['name_en']
            print(f"  [Book]: {b_id} | {book['name_hi']} / {book['name_en']}")

            if 'sections' in book:
                total_sections += len(book['sections'])
                for sec in book['sections']:
                    sec_id = sec['id']
                    assert sec_id not in all_ids, f"Duplicate ID: {sec_id}"
                    all_ids.add(sec_id)
                    assert sec['name_hi'] and sec['name_en']
                    print(f"    [Section]: {sec_id} | {sec['name_hi']} / {sec['name_en']}")

            total_chapters += len(book['chapters'])
            for ch in book['chapters']:
                c_id = ch['id']
                assert c_id not in all_ids, f"Duplicate ID: {c_id}"
                all_ids.add(c_id)
                assert ch['name_hi'] and ch['name_en']
                total_topics += len(ch['topics'])
                assert len(ch['topics']) > 0, f"Chapter {c_id} has 0 topics"
                for tp in ch['topics']:
                    tp_id = tp['id']
                    assert tp_id not in all_ids, f"Duplicate ID: {tp_id}"
                    all_ids.add(tp_id)
                    assert tp['name_hi'] and tp['name_en']

    print("\n" + "="*55)
    print("ALL INTEGRITY CHECKS PASSED SUCCESSFULLY!")
    print(f"Total Subjects:          {total_subs}")
    print(f"Total Books:             {total_books}")
    print(f"Total Sections:          {total_sections}")
    print(f"Total Chapters:          {total_chapters}")
    print(f"Total Topics/Subtopics:  {total_topics}")
    print(f"Total Unique Entities:   {len(all_ids)}")
    print("="*55)

if __name__ == '__main__':
    verify()
