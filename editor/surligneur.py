# -*- coding: utf-8 -*-
"""
Created on Mon May 31 08:17:26 2021

@author: Elvis
"""

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import Qt

class Surligneur(QSyntaxHighlighter):
    def __init__(self,parent = 0):
        super().__init__(QTextDocument())
        self.highlightingRules = list()

        self.commentStartExpression = QRegularExpression()
        self.commentEndExpression = QRegularExpression ()

        self.keywordFormat = QTextCharFormat()
        
        self.classFormat = QTextCharFormat()
        self.singleLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat = QTextCharFormat()
        self.quotationFormat = QTextCharFormat()
        self.functionFormat = QTextCharFormat()
        
        self.init_()
        
    def init_(self):
        rule = highlightingRule()
        self.keywordFormat.setForeground(Qt.darkBlue)
        self.keywordFormat.setFontWeight(QFont.Bold)
        
        keywordPatterns = list()
        keywordPatterns.append("\\band\\b")
        keywordPatterns.append("\\bdel\\b")
        keywordPatterns.append("\\bfrom\\b")
        keywordPatterns.append("\\bnone\\b")
        keywordPatterns.append("\\btrue\\b")
        keywordPatterns.append("\\bas\\b")
        keywordPatterns.append("\\belif\\b")
        keywordPatterns.append("\\bglobal\\b")
        keywordPatterns.append("\\bnonlocal\\b")
        keywordPatterns.append("\\btry\\b")
        keywordPatterns.append("\\bassert\\b")
        keywordPatterns.append("\\belse\\b")
        keywordPatterns.append("\\bif\\b")
        keywordPatterns.append("\\bnot\\b")
        keywordPatterns.append("\\bwhile\\b")
        keywordPatterns.append("\\bbreak\\b")
        keywordPatterns.append("\\bexcept\\b")
        keywordPatterns.append("\\bimport\\b")
        keywordPatterns.append("\\bor\\b")
        keywordPatterns.append("\\bwith\\b")
        keywordPatterns.append("\\bclass\\b")
        keywordPatterns.append("\\bfalse\\b")
        keywordPatterns.append("\\bin\\b")
        keywordPatterns.append("\\bpass\b")
        keywordPatterns.append("\\byield\\b")
        keywordPatterns.append("\\bcontinue\\b")
        keywordPatterns.append("\\bfinally\\b")
        keywordPatterns.append("\\bis\\b")
        keywordPatterns.append("\\braise\\b")
        keywordPatterns.append("\\bdef\\b")
        keywordPatterns.append("\\bfor\\b")
        keywordPatterns.append("\\blambda\\b")
        keywordPatterns.append("\\breturn\\b")
        
        for i in range(len(keywordPatterns)):
            rule.pattern = QRegularExpression(keywordPatterns[i])
            rule.format = self.keywordFormat
            self.highlightingRules.append(rule)
            
            
        self.classFormat.setFontWeight(QFont.Bold)
        #self.classFormat.setForeGround(Qt.darkMagenta)
        rule.pattern = QRegularExpression("\\bQ[A-Za-z]+\\b")
        rule.format = self.classFormat
        self.highlightingRules.append(rule)
        
        
    def highlightBlock(self,text):
        for rule in self.highlightingRules:
            matchIterator = rule.pattern.globalMacht(text)
            while matchIterator.hasNext():
                match = matchIterator.next()
                self.setFormat(match.capturedStart(),
                               match.capturedLength(), 
                               rule.format)
                
        self.setCurrentBlockState(0)
        startIndex = 0;
        if(self.previousBlockState() != 1):
            startIndex = text.indexOf(self.commentStartExpression)
            
        while (startIndex >= 0):
            match = self.commentEndExpression.match(text, startIndex);
            endIndex = match.capturedStart()
            commentLength = 0
            if (endIndex == -1):
                setCurrentBlockState(1)
                commentLength = text.length() - startIndex
            else:
                commentLength = endIndex - startIndex + match.capturedLength()
                
            self.setFormat(startIndex, commentLength, multiLineCommentFormat)
            startIndex = text.indexOf(commentStartExpression, startIndex + commentLength)  
        
class highlightingRule():
    def __init__(self):
        super().__init__()
        pattern = QRegularExpression()
        format = QTextCharFormat()
        
if __name__ == "__main__":
    """
    app = QApplication(sys.argv)
    w = Surligneur()
    w.show()
    sys.exit(app.exec_())
    """