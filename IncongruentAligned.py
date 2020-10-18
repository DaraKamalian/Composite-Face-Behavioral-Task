import random, csv, glob

from psychopy import core, event
from Window import window
from MainAssets import MainAssets

from MenAlign import Men_Align
from WomenAlign import Women_Align
from MenMisalign import Men_Misalign
from WomenMisalign import Women_Misalign
from SameUpperLocationsList import SameUpperLocationsList
from SameLowerLocationsList import SameLowerLocationsList

image = MainAssets()
correct = image.correct
wrong = image.wrong
women_align_images = Women_Align().women_align_images
women_align_locations = Women_Align().women_align_locations
men_align_images = Men_Align().men_align_images
men_align_locations = Men_Align().men_align_locations
women_misalign_images = Women_Misalign().women_misalign_images
women_misalign_locations = Women_Misalign().women_misalign_locations
men_misalign_images = Men_Misalign().men_misalign_images
men_misalign_locations = Men_Misalign().men_misalign_locations

fixationPoint = image.fixationPoint
questionMark = image.questionMark
win = window.win

class Incongruent_Aligned(object):
    def IncongruentAligned(self, practice, same, gender, index):
        fixationPoint.draw()
        win.flip()
        core.wait(0.2)

        fixationPoint.autoDraw = False
        win.flip()
        core.wait(0.15)

        if same:
            if gender:
                print('inc-same-al-m')
            else:
                print('inc-same-al-f')
        else:
            if gender:
                print('inc-diff-al-m')
            else:
                print('inc-diff-al-f')


        rand1 = random.randint(0, 19)
        if gender:
            men_align_images[rand1].draw()
            print(men_align_images[rand1].image)
            win.flip()
            core.wait(0.2)
        else:
            women_align_images[rand1].draw()
            print(women_align_images[rand1].image)
            win.flip()
            core.wait(0.2)

        men_align_images[rand1].autoDraw = False
        women_align_images[rand1].autoDraw = False
        win.flip()
        core.wait(0.4)

        if gender:
            images = men_align_images
            locations = men_align_locations
        else:
            images = women_align_images
            locations = women_align_locations

        if same:
            obj = SameUpperLocationsList()
            newLocations = SameUpperLocationsList.SameUpperLocationsList(obj,
                locations, images[rand1].image)
            print('newlocations length is :' + str(len(newLocations)))

            if len(newLocations) == 1:
                newLocRand = 0
            else:
                newLocRand = random.randint(0, (len(newLocations) - 1))

                print('new loc rand is :' + str(newLocRand))
            # for item in newLocations:
            #     print(item)
            secondsamefacelist = []

            for item in images:
                if item.image == newLocations[newLocRand]:
                    item.draw()
                    win.flip()
                    secondsamefacelist.append(item)
                    # print(item.image)
                    break
            core.wait(0.5)
            secondsamefacelist[0].autoDraw = False
            questionMark.draw()
            win.flip()

        else:
            obj = SameLowerLocationsList()
            newLocations = SameLowerLocationsList.SameLowerLocationsList(obj,
                                                                         locations,
                                                                         images[rand1].image)
            print('newlocations length is :' + str(len(newLocations)))
            if len(newLocations) == 1:
                newLocRand = 0
            else:
                newLocRand = random.randint(0, (len(newLocations) - 1))
                print('new loc rand is :' + str(newLocRand))
            # for item in newLocations:
            #     print(item)
            seconddifffacelist = []
            for item in images:
                if item.image == newLocations[newLocRand]:
                    item.draw()
                    win.flip()
                    seconddifffacelist.append(item)
                    # print(item.image)
                    break
            core.wait(0.5)
            seconddifffacelist[0].autoDraw = False
            questionMark.draw()
            win.flip()

        countdown = core.CountdownTimer(1.5)
        lateflag = False
        anslist = []
        flag = True
        while flag:
            # keys = event.getKeys(keyList=['a', 'l'])
            keys = event.waitKeys(keyList=['a', 'l'], maxWait=1.5)
            if keys:
                for key in keys:
                    if key == 'a':
                        if practice:
                            correct.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            anslist.append('A')
                            # write to table
                            # print('correct')
                        flag = False
                    elif key == 'l':
                        if practice:
                            wrong.draw()
                            win.flip()
                            core.wait(2)
                        else:
                            anslist.append('L')
                            # write to table
                        flag = False
            elif countdown.getTime() <= 0:
                lateflag = True
                flag = False

            with open('CongruentAligned' + str(index) + '.csv', 'w', newline='') as file:
                Headers = ['Face_1', 'Face_2', 'Face_Gender', 'Congruency', 'Block', 'Trial', 'Alignment', 'Condition',
                           'Type', 'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time', 'Trial-Start', 'Key-Resp-Start']

                writer = csv.DictWriter(file, fieldnames=Headers)
                writer.writeheader()

                if same and gender and not lateflag:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Same + Bottom Different', 'Cor-Ans': 'A',
                                     'Key-Resp': str(anslist[0]).upper(), 'R-time': str(1.5 - countdown.getTime()),
                                     'Face_Gender': 'Male', 'Face_1': men_align_images[rand1].image[-13:-4],
                                     'Face_2': secondsamefacelist[0].image[-13:-4], 'Congruency': '0',
                                     'Type': 'Aligned Incongruent'})

                if same and not gender and not lateflag:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Same + Bottom Different', 'Cor-Ans': 'A',
                                     'Key-Resp': str(anslist[0]).upper(), 'R-time': str(1.5 - countdown.getTime()),
                                     'Face_Gender': 'Female', 'Face_1': women_align_images[rand1].image[-13:-4],
                                     'Face_2': secondsamefacelist[0].image[-13:-4], 'Congruency': '0',
                                     'Type': 'Aligned Incongruent'})

                if not same and gender and not lateflag:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Different + Bottom Same', 'Cor-Ans': 'L',
                                     'Key-Resp': str(anslist[0]).upper(), 'R-time': str(1.5 - countdown.getTime()),
                                     'Face_Gender': 'Male', 'Face_1': men_align_images[rand1].image[-13:-4],
                                     'Face_2': seconddifffacelist[0].image[-13:-4], 'Congruency': '0',
                                     'Type': 'Aligned Incongruent'})


                if not same and not gender and not lateflag:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Different + Bottom Same', 'Cor-Ans': 'L',
                                     'Key-Resp': str(anslist[0]).upper(), 'R-time': str(1.5 - countdown.getTime()),
                                     'Face_Gender': 'Female', 'Face_1': women_align_images[rand1].image[-13:-4],
                                     'Face_2': seconddifffacelist[0].image[-13:-4], 'Congruency': '0',
                                     'Type': 'Aligned Incongruent'})

                if same and gender and lateflag:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Same + Bottom Different', 'Cor-Ans': 'A',
                                     'Key-Resp': 'None', 'R-time': 'None',
                                     'Face_Gender': 'Male', 'Face_1': men_align_images[rand1].image[-13:-4],
                                     'Face_2': secondsamefacelist[0].image[-13:-4], 'Congruency': '0',
                                     'Type': 'Aligned Incongruent'})

                if same and not gender and lateflag:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Same + Bottom Different', 'Cor-Ans': 'A',
                                     'Key-Resp': 'None', 'R-time': 'None',
                                     'Face_Gender': 'Female', 'Face_1': women_align_images[rand1].image[-13:-4],
                                     'Face_2': secondsamefacelist[0].image[-13:-4], 'Congruency': '0',
                                     'Type': 'Aligned Incongruent'})

                if not same and gender and lateflag:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Different + Bottom Same', 'Cor-Ans': 'L',
                                     'Key-Resp': 'None', 'R-time': 'None',
                                     'Face_Gender': 'Male', 'Face_1': men_align_images[rand1].image[-13:-4],
                                     'Face_2': seconddifffacelist[0].image[-13:-4], 'Congruency': '0',
                                     'Type': 'Aligned Incongruent'})


                if not same and not gender and lateflag:
                    writer.writerow({'Alignment': '1', 'Condition': 'Top Different + Bottom Same', 'Cor-Ans': 'L',
                                     'Key-Resp': 'None', 'R-time': 'None',
                                     'Face_Gender': 'Female', 'Face_1': women_align_images[rand1].image[-13:-4],
                                     'Face_2': seconddifffacelist[0].image[-13:-4], 'Congruency': '0',
                                     'Type': 'Aligned Incongruent'})


