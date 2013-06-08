# -*- coding: utf-8 -*-
#
# spec.py
#
# Copyright (C) 2012, 2013 Steve Canny scanny@cisco.com
#
# This module is part of python-pptx and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""
Constant values from the ECMA-376 spec that are needed for XML generation and
packaging, and a utility function or two for accessing some of them.
"""

from constants import (
    MSO_AUTO_SHAPE_TYPE as MAST, MSO, PP, TEXT_ALIGN_TYPE as TAT,
    TEXT_ANCHORING_TYPE as TANC
)


class VerticalAnchor(object):
    """
    Mappings between ``MsoVerticalAnchor`` values used in the API and
    ``ST_TextAnchoringType`` values used in the XML. ``MsoVerticalAnchor``
    values are like ``MSO.ANCHOR_MIDDLE``.
    """
    _mapping = {
        MSO.ANCHOR_TOP:    TANC.TOP,
        MSO.ANCHOR_MIDDLE: TANC.MIDDLE,
        MSO.ANCHOR_BOTTOM: TANC.BOTTOM
    }

    @classmethod
    def from_text_anchoring_type(cls, text_anchoring_type):
        """
        Map an ``ST_TextAnchoringType`` value (e.g. ``TANC.TOP`` or
        ``'t'``) to an MsoVerticalAnchor value (e.g. ``MSO.ANCHOR_TOP``).
        Returns |None| if *text_anchoring_type* is |None|.
        """
        if text_anchoring_type is None:
            return None
        for vertical_anchor, tanc in cls._mapping.iteritems():
            if tanc == text_anchoring_type:
                return vertical_anchor
        tmpl = "no vertical anchor type for ST_TextAnchoringType '%s'"
        raise KeyError(tmpl % text_anchoring_type)

    @classmethod
    def to_text_anchoring_type(cls, vertical_anchor):
        """
        Map an ``MsoVerticalAnchor`` value (e.g. ``MSO.ANCHOR_MIDDLE``) to an
        ``ST_TextAnchoringType`` value (e.g. ``TANC.MIDDLE`` or ``'ctr'``).
        Returns None if *vertical_anchor* is None.
        """
        if vertical_anchor is None:
            return None
        try:
            text_anchoring_type = cls._mapping[vertical_anchor]
        except KeyError:
            tmpl = "no ST_TextAnchoringType value for vertical_anchor '%s'"
            raise KeyError(tmpl % vertical_anchor)
        return text_anchoring_type


class ParagraphAlignment(object):
    """
    Mappings between ``PpParagraphAlignment`` values used in the API and
    ``ST_TextAlignType`` values used in the XML. ``PpParagraphAlignment``
    values are like ``PP.ALIGN_CENTER``.
    """
    _mapping = {
        PP.ALIGN_CENTER:          TAT.CENTER,
        PP.ALIGN_DISTRIBUTE:      TAT.DISTRIBUTE,
        PP.ALIGN_JUSTIFY:         TAT.JUSTIFY,
        PP.ALIGN_JUSTIFY_LOW:     TAT.JUSTIFY_LOW,
        PP.ALIGN_LEFT:            TAT.LEFT,
        PP.ALIGN_RIGHT:           TAT.RIGHT,
        PP.ALIGN_THAI_DISTRIBUTE: TAT.THAI_DISTRIBUTE
    }

    @classmethod
    def from_text_align_type(cls, text_align_type):
        """
        Map an ``ST_TextAlignType`` value (e.g. ``TAT.CENTER`` or ``'ctr'``)
        to a paragraph alignment value (e.g. ``PP.ALIGN_CENTER``). Returns
        None if *text_align_type* is None.
        """
        if text_align_type is None:
            return None
        for alignment, tat in cls._mapping.iteritems():
            if tat == text_align_type:
                return alignment
        tmpl = "no ST_TextAlignType '%s'"
        raise KeyError(tmpl % text_align_type)

    @classmethod
    def to_text_align_type(cls, alignment):
        """
        Map a paragraph alignment value (e.g. ``PP.ALIGN_CENTER``) to an
        ``ST_TextAlignType`` value (e.g. ``TAT.CENTER`` or ``'ctr'``).
        Returns None if *alignment* is None.
        """
        if alignment is None:
            return None
        try:
            text_align_type = cls._mapping[alignment]
        except KeyError:
            tmpl = "no ST_TextAlignType value for alignment '%s'"
            raise KeyError(tmpl % alignment)
        return text_align_type


# ============================================================================
# AutoShape type specs
# ============================================================================

autoshape_types = {
    MAST.ACTION_BUTTON_BACK_OR_PREVIOUS: {
        'basename': 'Action Button: Back or Previous',
        'prst':     'actionButtonBackPrevious',
    },
    MAST.ACTION_BUTTON_BEGINNING: {
        'basename': 'Action Button: Beginning',
        'prst':     'actionButtonBeginning',
    },
    MAST.ACTION_BUTTON_CUSTOM: {
        'basename': 'Action Button: Custom',
        'prst':     'actionButtonBlank',
    },
    MAST.ACTION_BUTTON_DOCUMENT: {
        'basename': 'Action Button: Document',
        'prst':     'actionButtonDocument',
    },
    MAST.ACTION_BUTTON_END: {
        'basename': 'Action Button: End',
        'prst':     'actionButtonEnd',
    },
    MAST.ACTION_BUTTON_FORWARD_OR_NEXT: {
        'basename': 'Action Button: Forward or Next',
        'prst':     'actionButtonForwardNext',
    },
    MAST.ACTION_BUTTON_HELP: {
        'basename': 'Action Button: Help',
        'prst':     'actionButtonHelp',
    },
    MAST.ACTION_BUTTON_HOME: {
        'basename': 'Action Button: Home',
        'prst':     'actionButtonHome',
    },
    MAST.ACTION_BUTTON_INFORMATION: {
        'basename': 'Action Button: Information',
        'prst':     'actionButtonInformation',
    },
    MAST.ACTION_BUTTON_MOVIE: {
        'basename': 'Action Button: Movie',
        'prst':     'actionButtonMovie',
    },
    MAST.ACTION_BUTTON_RETURN: {
        'basename': 'Action Button: Return',
        'prst':     'actionButtonReturn',
    },
    MAST.ACTION_BUTTON_SOUND: {
        'basename': 'Action Button: Sound',
        'prst':     'actionButtonSound',
    },
    MAST.ARC: {
        'basename': 'Arc',
        'prst':     'arc',
    },
    MAST.BALLOON: {
        'basename': 'Rounded Rectangular Callout',
        'prst':     'wedgeRoundRectCallout',
    },
    MAST.BENT_ARROW: {
        'basename': 'Bent Arrow',
        'prst':     'bentArrow',
    },
    MAST.BENT_UP_ARROW: {
        'basename': 'Bent-Up Arrow',
        'prst':     'bentUpArrow',
    },
    MAST.BEVEL: {
        'basename': 'Bevel',
        'prst':     'bevel',
    },
    MAST.BLOCK_ARC: {
        'basename': 'Block Arc',
        'prst':     'blockArc',
    },
    MAST.CAN: {
        'basename': 'Can',
        'prst':     'can',
    },
    MAST.CHART_PLUS: {
        'basename': 'Chart Plus',
        'prst':     'chartPlus',
    },
    MAST.CHART_STAR: {
        'basename': 'Chart Star',
        'prst':     'chartStar',
    },
    MAST.CHART_X: {
        'basename': 'Chart X',
        'prst':     'chartX',
    },
    MAST.CHEVRON: {
        'basename': 'Chevron',
        'prst':     'chevron',
    },
    MAST.CHORD: {
        'basename': 'Chord',
        'prst':     'chord',
    },
    MAST.CIRCULAR_ARROW: {
        'basename': 'Circular Arrow',
        'prst':     'circularArrow',
    },
    MAST.CLOUD: {
        'basename': 'Cloud',
        'prst':     'cloud',
    },
    MAST.CLOUD_CALLOUT: {
        'basename': 'Cloud Callout',
        'prst':     'cloudCallout',
    },
    MAST.CORNER: {
        'basename': 'Corner',
        'prst':     'corner',
    },
    MAST.CORNER_TABS: {
        'basename': 'Corner Tabs',
        'prst':     'cornerTabs',
    },
    MAST.CROSS: {
        'basename': 'Cross',
        'prst':     'plus',
    },
    MAST.CUBE: {
        'basename': 'Cube',
        'prst':     'cube',
    },
    MAST.CURVED_DOWN_ARROW: {
        'basename': 'Curved Down Arrow',
        'prst':     'curvedDownArrow',
    },
    MAST.CURVED_DOWN_RIBBON: {
        'basename': 'Curved Down Ribbon',
        'prst':     'ellipseRibbon',
    },
    MAST.CURVED_LEFT_ARROW: {
        'basename': 'Curved Left Arrow',
        'prst':     'curvedLeftArrow',
    },
    MAST.CURVED_RIGHT_ARROW: {
        'basename': 'Curved Right Arrow',
        'prst':     'curvedRightArrow',
    },
    MAST.CURVED_UP_ARROW: {
        'basename': 'Curved Up Arrow',
        'prst':     'curvedUpArrow',
    },
    MAST.CURVED_UP_RIBBON: {
        'basename': 'Curved Up Ribbon',
        'prst':     'ellipseRibbon2',
    },
    MAST.DECAGON: {
        'basename': 'Decagon',
        'prst':     'decagon',
    },
    MAST.DIAGONAL_STRIPE: {
        'basename': 'Diagonal Stripe',
        'prst':     'diagStripe',
    },
    MAST.DIAMOND: {
        'basename': 'Diamond',
        'prst':     'diamond',
    },
    MAST.DODECAGON: {
        'basename': 'Dodecagon',
        'prst':     'dodecagon',
    },
    MAST.DONUT: {
        'basename': 'Donut',
        'prst':     'donut',
    },
    MAST.DOUBLE_BRACE: {
        'basename': 'Double Brace',
        'prst':     'bracePair',
    },
    MAST.DOUBLE_BRACKET: {
        'basename': 'Double Bracket',
        'prst':     'bracketPair',
    },
    MAST.DOUBLE_WAVE: {
        'basename': 'Double Wave',
        'prst':     'doubleWave',
    },
    MAST.DOWN_ARROW: {
        'basename': 'Down Arrow',
        'prst':     'downArrow',
    },
    MAST.DOWN_ARROW_CALLOUT: {
        'basename': 'Down Arrow Callout',
        'prst':     'downArrowCallout',
    },
    MAST.DOWN_RIBBON: {
        'basename': 'Down Ribbon',
        'prst':     'ribbon',
    },
    MAST.EXPLOSION1: {
        'basename': 'Explosion',
        'prst':     'irregularSeal1',
    },
    MAST.EXPLOSION2: {
        'basename': 'Explosion',
        'prst':     'irregularSeal2',
    },
    MAST.FLOWCHART_ALTERNATE_PROCESS: {
        'basename': 'Alternate process',
        'prst':     'flowChartAlternateProcess',
    },
    MAST.FLOWCHART_CARD: {
        'basename': 'Card',
        'prst':     'flowChartPunchedCard',
    },
    MAST.FLOWCHART_COLLATE: {
        'basename': 'Collate',
        'prst':     'flowChartCollate',
    },
    MAST.FLOWCHART_CONNECTOR: {
        'basename': 'Connector',
        'prst':     'flowChartConnector',
    },
    MAST.FLOWCHART_DATA: {
        'basename': 'Data',
        'prst':     'flowChartInputOutput',
    },
    MAST.FLOWCHART_DECISION: {
        'basename': 'Decision',
        'prst':     'flowChartDecision',
    },
    MAST.FLOWCHART_DELAY: {
        'basename': 'Delay',
        'prst':     'flowChartDelay',
    },
    MAST.FLOWCHART_DIRECT_ACCESS_STORAGE: {
        'basename': 'Direct Access Storage',
        'prst':     'flowChartMagneticDrum',
    },
    MAST.FLOWCHART_DISPLAY: {
        'basename': 'Display',
        'prst':     'flowChartDisplay',
    },
    MAST.FLOWCHART_DOCUMENT: {
        'basename': 'Document',
        'prst':     'flowChartDocument',
    },
    MAST.FLOWCHART_EXTRACT: {
        'basename': 'Extract',
        'prst':     'flowChartExtract',
    },
    MAST.FLOWCHART_INTERNAL_STORAGE: {
        'basename': 'Internal Storage',
        'prst':     'flowChartInternalStorage',
    },
    MAST.FLOWCHART_MAGNETIC_DISK: {
        'basename': 'Magnetic Disk',
        'prst':     'flowChartMagneticDisk',
    },
    MAST.FLOWCHART_MANUAL_INPUT: {
        'basename': 'Manual Input',
        'prst':     'flowChartManualInput',
    },
    MAST.FLOWCHART_MANUAL_OPERATION: {
        'basename': 'Manual Operation',
        'prst':     'flowChartManualOperation',
    },
    MAST.FLOWCHART_MERGE: {
        'basename': 'Merge',
        'prst':     'flowChartMerge',
    },
    MAST.FLOWCHART_MULTIDOCUMENT: {
        'basename': 'Multidocument',
        'prst':     'flowChartMultidocument',
    },
    MAST.FLOWCHART_OFFLINE_STORAGE: {
        'basename': 'Offline Storage',
        'prst':     'flowChartOfflineStorage',
    },
    MAST.FLOWCHART_OFFPAGE_CONNECTOR: {
        'basename': 'Off-page Connector',
        'prst':     'flowChartOffpageConnector',
    },
    MAST.FLOWCHART_OR: {
        'basename': 'Or',
        'prst':     'flowChartOr',
    },
    MAST.FLOWCHART_PREDEFINED_PROCESS: {
        'basename': 'Predefined Process',
        'prst':     'flowChartPredefinedProcess',
    },
    MAST.FLOWCHART_PREPARATION: {
        'basename': 'Preparation',
        'prst':     'flowChartPreparation',
    },
    MAST.FLOWCHART_PROCESS: {
        'basename': 'Process',
        'prst':     'flowChartProcess',
    },
    MAST.FLOWCHART_PUNCHED_TAPE: {
        'basename': 'Punched Tape',
        'prst':     'flowChartPunchedTape',
    },
    MAST.FLOWCHART_SEQUENTIAL_ACCESS_STORAGE: {
        'basename': 'Sequential Access Storage',
        'prst':     'flowChartMagneticTape',
    },
    MAST.FLOWCHART_SORT: {
        'basename': 'Sort',
        'prst':     'flowChartSort',
    },
    MAST.FLOWCHART_STORED_DATA: {
        'basename': 'Stored Data',
        'prst':     'flowChartOnlineStorage',
    },
    MAST.FLOWCHART_SUMMING_JUNCTION: {
        'basename': 'Summing Junction',
        'prst':     'flowChartSummingJunction',
    },
    MAST.FLOWCHART_TERMINATOR: {
        'basename': 'Terminator',
        'prst':     'flowChartTerminator',
    },
    MAST.FOLDED_CORNER: {
        'basename': 'Folded Corner',
        'prst':     'folderCorner',
    },
    MAST.FRAME: {
        'basename': 'Frame',
        'prst':     'frame',
    },
    MAST.FUNNEL: {
        'basename': 'Funnel',
        'prst':     'funnel',
    },
    MAST.GEAR_6: {
        'basename': 'Gear 6',
        'prst':     'gear6',
    },
    MAST.GEAR_9: {
        'basename': 'Gear 9',
        'prst':     'gear9',
    },
    MAST.HALF_FRAME: {
        'basename': 'Half Frame',
        'prst':     'halfFrame',
    },
    MAST.HEART: {
        'basename': 'Heart',
        'prst':     'heart',
    },
    MAST.HEPTAGON: {
        'basename': 'Heptagon',
        'prst':     'heptagon',
    },
    MAST.HEXAGON: {
        'basename': 'Hexagon',
        'prst':     'hexagon',
    },
    MAST.HORIZONTAL_SCROLL: {
        'basename': 'Horizontal Scroll',
        'prst':     'horizontalScroll',
    },
    MAST.ISOSCELES_TRIANGLE: {
        'basename': 'Isosceles Triangle',
        'prst':     'triangle',
    },
    MAST.LEFT_ARROW: {
        'basename': 'Left Arrow',
        'prst':     'leftArrow',
    },
    MAST.LEFT_ARROW_CALLOUT: {
        'basename': 'Left Arrow Callout',
        'prst':     'leftArrowCallout',
    },
    MAST.LEFT_BRACE: {
        'basename': 'Left Brace',
        'prst':     'leftBrace',
    },
    MAST.LEFT_BRACKET: {
        'basename': 'Left Bracket',
        'prst':     'leftBracket',
    },
    MAST.LEFT_CIRCULAR_ARROW: {
        'basename': 'Left Circular Arrow',
        'prst':     'leftCircularArrow',
    },
    MAST.LEFT_RIGHT_ARROW: {
        'basename': 'Left-Right Arrow',
        'prst':     'leftRightArrow',
    },
    MAST.LEFT_RIGHT_ARROW_CALLOUT: {
        'basename': 'Left-Right Arrow Callout',
        'prst':     'leftRightArrowCallout',
    },
    MAST.LEFT_RIGHT_CIRCULAR_ARROW: {
        'basename': 'Left Right Circular Arrow',
        'prst':     'leftRightCircularArrow',
    },
    MAST.LEFT_RIGHT_RIBBON: {
        'basename': 'Left Right Ribbon',
        'prst':     'leftRightRibbon',
    },
    MAST.LEFT_RIGHT_UP_ARROW: {
        'basename': 'Left-Right-Up Arrow',
        'prst':     'leftRightUpArrow',
    },
    MAST.LEFT_UP_ARROW: {
        'basename': 'Left-Up Arrow',
        'prst':     'leftUpArrow',
    },
    MAST.LIGHTNING_BOLT: {
        'basename': 'Lightning Bolt',
        'prst':     'lightningBolt',
    },
    MAST.LINE_CALLOUT_1: {
        'basename': 'Line Callout 1',
        'prst':     'borderCallout1',
    },
    MAST.LINE_CALLOUT_1_ACCENT_BAR: {
        'basename': 'Line Callout 1 (Accent Bar)',
        'prst':     'accentCallout1',
    },
    MAST.LINE_CALLOUT_1_BORDER_AND_ACCENT_BAR: {
        'basename': 'Line Callout 1 (Border and Accent Bar)',
        'prst':     'accentBorderCallout1',
    },
    MAST.LINE_CALLOUT_1_NO_BORDER: {
        'basename': 'Line Callout 1 (No Border)',
        'prst':     'callout1',
    },
    MAST.LINE_CALLOUT_2: {
        'basename': 'Line Callout 2',
        'prst':     'borderCallout2',
    },
    MAST.LINE_CALLOUT_2_ACCENT_BAR: {
        'basename': 'Line Callout 2 (Accent Bar)',
        'prst':     'accentCallout2',
    },
    MAST.LINE_CALLOUT_2_BORDER_AND_ACCENT_BAR: {
        'basename': 'Line Callout 2 (Border and Accent Bar)',
        'prst':     'accentBorderCallout2',
    },
    MAST.LINE_CALLOUT_2_NO_BORDER: {
        'basename': 'Line Callout 2 (No Border)',
        'prst':     'callout2',
    },
    MAST.LINE_CALLOUT_3: {
        'basename': 'Line Callout 3',
        'prst':     'borderCallout3',
    },
    MAST.LINE_CALLOUT_3_ACCENT_BAR: {
        'basename': 'Line Callout 3 (Accent Bar)',
        'prst':     'accentCallout3',
    },
    MAST.LINE_CALLOUT_3_BORDER_AND_ACCENT_BAR: {
        'basename': 'Line Callout 3 (Border and Accent Bar)',
        'prst':     'accentBorderCallout3',
    },
    MAST.LINE_CALLOUT_3_NO_BORDER: {
        'basename': 'Line Callout 3 (No Border)',
        'prst':     'callout3',
    },
    MAST.LINE_CALLOUT_4: {
        'basename': 'Line Callout 3',
        'prst':     'borderCallout3',
    },
    MAST.LINE_CALLOUT_4_ACCENT_BAR: {
        'basename': 'Line Callout 3 (Accent Bar)',
        'prst':     'accentCallout3',
    },
    MAST.LINE_CALLOUT_4_BORDER_AND_ACCENT_BAR: {
        'basename': 'Line Callout 3 (Border and Accent Bar)',
        'prst':     'accentBorderCallout3',
    },
    MAST.LINE_CALLOUT_4_NO_BORDER: {
        'basename': 'Line Callout 3 (No Border)',
        'prst':     'callout3',
    },
    MAST.LINE_INVERSE: {
        'basename': 'Straight Connector',
        'prst':     'lineInv',
    },
    MAST.MATH_DIVIDE: {
        'basename': 'Division',
        'prst':     'mathDivide',
    },
    MAST.MATH_EQUAL: {
        'basename': 'Equal',
        'prst':     'mathEqual',
    },
    MAST.MATH_MINUS: {
        'basename': 'Minus',
        'prst':     'mathMinus',
    },
    MAST.MATH_MULTIPLY: {
        'basename': 'Multiply',
        'prst':     'mathMultiply',
    },
    MAST.MATH_NOT_EQUAL: {
        'basename': 'Not Equal',
        'prst':     'mathNotEqual',
    },
    MAST.MATH_PLUS: {
        'basename': 'Plus',
        'prst':     'mathPlus',
    },
    MAST.MOON: {
        'basename': 'Moon',
        'prst':     'moon',
    },
    MAST.NO_SYMBOL: {
        'basename': '"No" symbol',
        'prst':     'noSmoking',
    },
    MAST.NON_ISOSCELES_TRAPEZOID: {
        'basename': 'Non-isosceles Trapezoid',
        'prst':     'nonIsoscelesTrapezoid',
    },
    MAST.NOTCHED_RIGHT_ARROW: {
        'basename': 'Notched Right Arrow',
        'prst':     'notchedRightArrow',
    },
    MAST.OCTAGON: {
        'basename': 'Octagon',
        'prst':     'octagon',
    },
    MAST.OVAL: {
        'basename': 'Oval',
        'prst':     'ellipse',
    },
    MAST.OVAL_CALLOUT: {
        'basename': 'Oval Callout',
        'prst':     'wedgeEllipseCallout',
    },
    MAST.PARALLELOGRAM: {
        'basename': 'Parallelogram',
        'prst':     'parallelogram',
    },
    MAST.PENTAGON: {
        'basename': 'Pentagon',
        'prst':     'homePlate',
    },
    MAST.PIE: {
        'basename': 'Pie',
        'prst':     'pie',
    },
    MAST.PIE_WEDGE: {
        'basename': 'Pie',
        'prst':     'pieWedge',
    },
    MAST.PLAQUE: {
        'basename': 'Plaque',
        'prst':     'plaque',
    },
    MAST.PLAQUE_TABS: {
        'basename': 'Plaque Tabs',
        'prst':     'plaqueTabs',
    },
    MAST.QUAD_ARROW: {
        'basename': 'Quad Arrow',
        'prst':     'quadArrow',
    },
    MAST.QUAD_ARROW_CALLOUT: {
        'basename': 'Quad Arrow Callout',
        'prst':     'quadArrowCallout',
    },
    MAST.RECTANGLE: {
        'basename': 'Rectangle',
        'prst':     'rect',
    },
    MAST.RECTANGULAR_CALLOUT: {
        'basename': 'Rectangular Callout',
        'prst':     'wedgeRectCallout',
    },
    MAST.REGULAR_PENTAGON: {
        'basename': 'Regular Pentagon',
        'prst':     'pentagon',
    },
    MAST.RIGHT_ARROW: {
        'basename': 'Right Arrow',
        'prst':     'rightArrow',
    },
    MAST.RIGHT_ARROW_CALLOUT: {
        'basename': 'Right Arrow Callout',
        'prst':     'rightArrowCallout',
    },
    MAST.RIGHT_BRACE: {
        'basename': 'Right Brace',
        'prst':     'rightBrace',
    },
    MAST.RIGHT_BRACKET: {
        'basename': 'Right Bracket',
        'prst':     'rightBracket',
    },
    MAST.RIGHT_TRIANGLE: {
        'basename': 'Right Triangle',
        'prst':     'rtTriangle',
    },
    MAST.ROUND_1_RECTANGLE: {
        'basename': 'Round Single Corner Rectangle',
        'prst':     'round1Rect',
    },
    MAST.ROUND_2_DIAG_RECTANGLE: {
        'basename': 'Round Diagonal Corner Rectangle',
        'prst':     'round2DiagRect',
    },
    MAST.ROUND_2_SAME_RECTANGLE: {
        'basename': 'Round Same Side Corner Rectangle',
        'prst':     'round2SameRect',
    },
    MAST.ROUNDED_RECTANGLE: {
        'basename': 'Rounded Rectangle',
        'prst':     'roundRect',
    },
    MAST.ROUNDED_RECTANGULAR_CALLOUT: {
        'basename': 'Rounded Rectangular Callout',
        'prst':     'wedgeRoundRectCallout',
    },
    MAST.SMILEY_FACE: {
        'basename': 'Smiley Face',
        'prst':     'smileyFace',
    },
    MAST.SNIP_1_RECTANGLE: {
        'basename': 'Snip Single Corner Rectangle',
        'prst':     'snip1Rect',
    },
    MAST.SNIP_2_DIAG_RECTANGLE: {
        'basename': 'Snip Diagonal Corner Rectangle',
        'prst':     'snip2DiagRect',
    },
    MAST.SNIP_2_SAME_RECTANGLE: {
        'basename': 'Snip Same Side Corner Rectangle',
        'prst':     'snip2SameRect',
    },
    MAST.SNIP_ROUND_RECTANGLE: {
        'basename': 'Snip and Round Single Corner Rectangle',
        'prst':     'snipRoundRect',
    },
    MAST.SQUARE_TABS: {
        'basename': 'Square Tabs',
        'prst':     'squareTabs',
    },
    MAST.STAR_10_POINT: {
        'basename': '10-Point Star',
        'prst':     'star10',
    },
    MAST.STAR_12_POINT: {
        'basename': '12-Point Star',
        'prst':     'star12',
    },
    MAST.STAR_16_POINT: {
        'basename': '16-Point Star',
        'prst':     'star16',
    },
    MAST.STAR_24_POINT: {
        'basename': '24-Point Star',
        'prst':     'star24',
    },
    MAST.STAR_32_POINT: {
        'basename': '32-Point Star',
        'prst':     'star32',
    },
    MAST.STAR_4_POINT: {
        'basename': '4-Point Star',
        'prst':     'star4',
    },
    MAST.STAR_5_POINT: {
        'basename': '5-Point Star',
        'prst':     'star5',
    },
    MAST.STAR_6_POINT: {
        'basename': '6-Point Star',
        'prst':     'star6',
    },
    MAST.STAR_7_POINT: {
        'basename': '7-Point Star',
        'prst':     'star7',
    },
    MAST.STAR_8_POINT: {
        'basename': '8-Point Star',
        'prst':     'star8',
    },
    MAST.STRIPED_RIGHT_ARROW: {
        'basename': 'Striped Right Arrow',
        'prst':     'stripedRightArrow',
    },
    MAST.SUN: {
        'basename': 'Sun',
        'prst':     'sun',
    },
    MAST.SWOOSH_ARROW: {
        'basename': 'Swoosh Arrow',
        'prst':     'swooshArrow',
    },
    MAST.TEAR: {
        'basename': 'Teardrop',
        'prst':     'teardrop',
    },
    MAST.TRAPEZOID: {
        'basename': 'Trapezoid',
        'prst':     'trapezoid',
    },
    MAST.U_TURN_ARROW: {
        'basename': 'U-Turn Arrow',
        'prst':     'uturnArrow',
    },
    MAST.UP_ARROW: {
        'basename': 'Up Arrow',
        'prst':     'upArrow',
    },
    MAST.UP_ARROW_CALLOUT: {
        'basename': 'Up Arrow Callout',
        'prst':     'upArrowCallout',
    },
    MAST.UP_DOWN_ARROW: {
        'basename': 'Up-Down Arrow',
        'prst':     'upDownArrow',
    },
    MAST.UP_DOWN_ARROW_CALLOUT: {
        'basename': 'Up-Down Arrow Callout',
        'prst':     'upDownArrowCallout',
    },
    MAST.UP_RIBBON: {
        'basename': 'Up Ribbon',
        'prst':     'ribbon2',
    },
    MAST.VERTICAL_SCROLL: {
        'basename': 'Vertical Scroll',
        'prst':     'verticalScroll',
    },
    MAST.WAVE: {
        'basename': 'Wave',
        'prst':     'wave',
    }
}


# ============================================================================
# Placeholder constants
# ============================================================================

# valid values for <p:ph> type attribute (ST_PlaceholderType)
# -----------------------------------------------------------
PH_TYPE_TITLE = 'title'
PH_TYPE_BODY = 'body'
PH_TYPE_CTRTITLE = 'ctrTitle'
PH_TYPE_SUBTITLE = 'subTitle'
PH_TYPE_DT = 'dt'
PH_TYPE_SLDNUM = 'sldNum'
PH_TYPE_FTR = 'ftr'
PH_TYPE_HDR = 'hdr'
PH_TYPE_OBJ = 'obj'
PH_TYPE_CHART = 'chart'
PH_TYPE_TBL = 'tbl'
PH_TYPE_CLIPART = 'clipArt'
PH_TYPE_DGM = 'dgm'
PH_TYPE_MEDIA = 'media'
PH_TYPE_SLDIMG = 'sldImg'
PH_TYPE_PIC = 'pic'

# valid values for <p:ph> orient attribute
# ----------------------------------------
PH_ORIENT_HORZ = 'horz'
PH_ORIENT_VERT = 'vert'

# valid values for <p:ph> sz (size) attribute
# -------------------------------------------
PH_SZ_FULL = 'full'
PH_SZ_HALF = 'half'
PH_SZ_QUARTER = 'quarter'

# mapping of type to rootname (part of auto-generated placeholder shape name)
slide_ph_basenames = {
    PH_TYPE_TITLE:    'Title',
    # this next one is named 'Notes Placeholder' in a notes master
    PH_TYPE_BODY:     'Text Placeholder',
    PH_TYPE_CTRTITLE: 'Title',
    PH_TYPE_SUBTITLE: 'Subtitle',
    PH_TYPE_DT:       'Date Placeholder',
    PH_TYPE_SLDNUM:   'Slide Number Placeholder',
    PH_TYPE_FTR:      'Footer Placeholder',
    PH_TYPE_HDR:      'Header Placeholder',
    PH_TYPE_OBJ:      'Content Placeholder',
    PH_TYPE_CHART:    'Chart Placeholder',
    PH_TYPE_TBL:      'Table Placeholder',
    PH_TYPE_CLIPART:  'ClipArt Placeholder',
    PH_TYPE_DGM:      'SmartArt Placeholder',
    PH_TYPE_MEDIA:    'Media Placeholder',
    PH_TYPE_SLDIMG:   'Slide Image Placeholder',
    PH_TYPE_PIC:      'Picture Placeholder'
}

# ============================================================================
# PresentationML Part Type specs
# ============================================================================
# Keyed by content type
# Not yet included:
# * Font Part (font1.fntdata) 15.2.13
# * themeOverride : 'application/vnd.openxmlformats-officedocument.'
#                   'themeOverride+xml'
# * several others, especially DrawingML parts ...
#
# TODO: Also check out other shared parts in section 15.
# ============================================================================

PTS_CARDINALITY_SINGLETON = 'singleton'
PTS_CARDINALITY_TUPLE = 'tuple'
PTS_HASRELS_ALWAYS = 'always'
PTS_HASRELS_NEVER = 'never'
PTS_HASRELS_OPTIONAL = 'optional'

CT_CHART = (
    'application/vnd.openxmlformats-officedocument.drawingml.chart+xml')
CT_COMMENT_AUTHORS = (
    'application/vnd.openxmlformats-officedocument.presentationml.commentAuth'
    'ors+xml')
CT_COMMENTS = (
    'application/vnd.openxmlformats-officedocument.presentationml.comments+xm'
    'l')
CT_CORE_PROPS = (
    'application/vnd.openxmlformats-package.core-properties+xml')
CT_CUSTOM_PROPS = (
    'application/vnd.openxmlformats-officedocument.custom-properties+xml')
CT_EXCEL_XLSX = (
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
CT_EXTENDED_PROPS = (
    'application/vnd.openxmlformats-officedocument.extended-properties+xml')
CT_HANDOUT_MASTER = (
    'application/vnd.openxmlformats-officedocument.presentationml.handoutMast'
    'er+xml')
CT_NOTES_MASTER = (
    'application/vnd.openxmlformats-officedocument.presentationml.notesMaster'
    '+xml')
CT_NOTES_SLIDE = (
    'application/vnd.openxmlformats-officedocument.presentationml.notesSlide+'
    'xml')
CT_PRES_PROPS = (
    'application/vnd.openxmlformats-officedocument.presentationml.presProps+x'
    'ml')
CT_PRESENTATION = (
    'application/vnd.openxmlformats-officedocument.presentationml.presentatio'
    'n.main+xml')
CT_PRINTER_SETTINGS = (
    'application/vnd.openxmlformats-officedocument.presentationml.printerSett'
    'ings')
CT_SLIDE = (
    'application/vnd.openxmlformats-officedocument.presentationml.slide+xml')
CT_SLIDE_LAYOUT = (
    'application/vnd.openxmlformats-officedocument.presentationml.slideLayout'
    '+xml')
CT_SLIDE_MASTER = (
    'application/vnd.openxmlformats-officedocument.presentationml.slideMaster'
    '+xml')
CT_SLIDESHOW = (
    'application/vnd.openxmlformats-officedocument.presentationml.slideshow.m'
    'ain+xml')
CT_TABLE_STYLES = (
    'application/vnd.openxmlformats-officedocument.presentationml.tableStyles'
    '+xml')
CT_TAGS = (
    'application/vnd.openxmlformats-officedocument.presentationml.tags+xml')
CT_TEMPLATE = (
    'application/vnd.openxmlformats-officedocument.presentationml.template.ma'
    'in+xml')
CT_THEME = (
    'application/vnd.openxmlformats-officedocument.theme+xml')
CT_VIEW_PROPS = (
    'application/vnd.openxmlformats-officedocument.presentationml.viewProps+x'
    'ml')
CT_WORKSHEET = (
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


RT_CHART = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/char'
    't')
RT_COMMENT_AUTHORS = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/comm'
    'entAuthors')
RT_COMMENTS = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/comm'
    'ents')
RT_CORE_PROPS = (
    'http://schemas.openxmlformats.org/officedocument/2006/relationships/meta'
    'data/core-properties')
RT_CUSTOM_PROPS = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/cust'
    'omProperties')
RT_EXTENDED_PROPS = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/exte'
    'ndedProperties')
RT_HANDOUT_MASTER = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hand'
    'outMaster')
RT_IMAGE = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/imag'
    'e')
RT_NOTES_MASTER = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/note'
    'sMaster')
RT_NOTES_SLIDE = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/note'
    'sSlide')
RT_OFFICE_DOCUMENT = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/offi'
    'ceDocument')
RT_PACKAGE = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/pack'
    'age')
RT_PRES_PROPS = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/pres'
    'Props')
RT_PRINTER_SETTINGS = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/prin'
    'terSettings')
RT_SLIDE = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/slid'
    'e')
RT_SLIDE_LAYOUT = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/slid'
    'eLayout')
RT_SLIDE_MASTER = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/slid'
    'eMaster')
RT_SLIDESHOW = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/offi'
    'ceDocument')
RT_TABLESTYLES = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/tabl'
    'eStyles')
RT_TAGS = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/tags')
RT_TEMPLATE = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/offi'
    'ceDocument')
RT_THEME = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/them'
    'e')
RT_VIEWPROPS = (
    'http://schemas.openxmlformats.org/officeDocument/2006/relationships/view'
    'Props')

pml_parttypes = {
    CT_COMMENT_AUTHORS: {  # ECMA-376-1 13.3.1
        'basename':    'commentAuthors',
        'ext':         '.xml',
        'name':        'Comment Authors Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    False,
        'baseURI':     '/ppt',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['presentation'],
        'reltype':     RT_COMMENT_AUTHORS},
    CT_COMMENTS: {  # ECMA-376-1 13.3.2
        'basename':    'comment',
        'ext':         '.xml',
        'name':        'Comments Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/comments',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['slide'],
        'reltype':     RT_COMMENTS},
    CT_CORE_PROPS: {  # ECMA-376-1 15.2.12.1 ('Core' as in Dublin Core)
        'basename':    'core',
        'ext':         '.xml',
        'name':        'Core File Properties Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    False,
        'baseURI':     '/docProps',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['package'],
        'reltype':     RT_CORE_PROPS},
    CT_CUSTOM_PROPS: {  # ECMA-376-1 15.2.12.2
        'basename':    'custom',
        'ext':         '.xml',
        'name':        'Custom File Properties Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    False,
        'baseURI':     '/docProps',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['package'],
        'reltype':     RT_CUSTOM_PROPS},
    CT_EXTENDED_PROPS: {  # ECMA-376-1 15.2.12.3 (Extended File Properties)
        'basename':    'app',
        'ext':         '.xml',
        'name':        'Application-Defined File Properties Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    False,
        'baseURI':     '/docProps',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['package'],
        'reltype':     RT_EXTENDED_PROPS},
    CT_HANDOUT_MASTER: {  # ECMA-376-1 13.3.3
        'basename':    'handoutMaster',
        'ext':         '.xml',
        'name':        'Handout Master Part',
        # actually can only be one according to spec, but behaves like part
        # collection (handoutMasters folder, handoutMaster1.xml, etc.)
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/handoutMasters',
        'has_rels':    PTS_HASRELS_ALWAYS,
        'rels_from':   ['presentation'],
        'reltype':     RT_HANDOUT_MASTER},
    CT_NOTES_MASTER: {  # ECMA-376-1 13.3.4
        'basename':    'notesMaster',
        'ext':         '.xml',
        'name':        'Notes Master Part',
        # actually can only be one according to spec, but behaves like part
        # collection (notesMasters folder, notesMaster1.xml, etc.)
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/notesMasters',
        'has_rels':    PTS_HASRELS_ALWAYS,
        'rels_from':   ['presentation', 'notesSlide'],
        'reltype':     RT_NOTES_MASTER},
    CT_NOTES_SLIDE: {  # ECMA-376-1 13.3.5
        'basename':    'notesSlide',
        'ext':         '.xml',
        'name':        'Notes Slide Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/notesSlides',
        'has_rels':    PTS_HASRELS_ALWAYS,
        'rels_from':   ['slide'],
        'reltype':     RT_NOTES_SLIDE},
    CT_PRESENTATION: {  # ECMA-376-1 13.3.6
        # one of three possible Content Type values for presentation part
        'basename':    'presentation',
        'ext':         '.xml',
        'name':        'Presentation Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    True,
        'baseURI':     '/ppt',
        'has_rels':    PTS_HASRELS_ALWAYS,
        'rels_from':   ['package'],
        'reltype':     RT_OFFICE_DOCUMENT},
    CT_PRES_PROPS: {  # ECMA-376-1 13.3.7
        'basename':    'presProps',
        'ext':         '.xml',
        'name':        'Presentation Properties Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    True,
        'baseURI':     '/ppt',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['presentation'],
        'reltype':     RT_PRES_PROPS},
    CT_PRINTER_SETTINGS: {  # ECMA-376-1 15.2.15
        'basename':    'printerSettings',
        'ext':         '.bin',
        'name':        'Printer Settings Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/printerSettings',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['presentation'],
        'reltype':     RT_PRINTER_SETTINGS},
    CT_SLIDE: {  # ECMA-376-1 13.3.8
        'basename':    'slide',
        'ext':         '.xml',
        'name':        'Slide Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/slides',
        'has_rels':    PTS_HASRELS_ALWAYS,
        'rels_from':   ['presentation', 'notesSlide'],
        'reltype':     RT_SLIDE},
    CT_SLIDE_LAYOUT: {  # ECMA-376-1 13.3.9
        'basename':    'slideLayout',
        'ext':         '.xml',
        'name':        'Slide Layout Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    True,
        'baseURI':     '/ppt/slideLayouts',
        'has_rels':    PTS_HASRELS_ALWAYS,
        'rels_from':   ['slide', 'slideMaster'],
        'reltype':     RT_SLIDE_LAYOUT},
    CT_SLIDE_MASTER: {  # ECMA-376-1 13.3.10
        'basename':    'slideMaster',
        'ext':         '.xml',
        'name':        'Slide Master Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    True,
        'baseURI':     '/ppt/slideMasters',
        'has_rels':    PTS_HASRELS_ALWAYS,
        'rels_from':   ['presentation', 'slideLayout'],
        'reltype':     RT_SLIDE_MASTER},
    CT_SLIDESHOW: {  # ECMA-376-1 13.3.6
        # one of three possible Content Type values for presentation part
        'basename':    'presentation',
        'ext':         '.xml',
        'name':        'Presentation Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    True,
        'baseURI':     '/ppt',
        'has_rels':    PTS_HASRELS_ALWAYS,
        'rels_from':   ['package'],
        'reltype':     RT_SLIDESHOW},
    CT_TABLE_STYLES: {  # ECMA-376-1 14.2.9
        'basename':    'tableStyles',
        'ext':         '.xml',
        'name':        'Table Styles Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    False,
        'baseURI':     '/ppt',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['presentation'],
        'reltype':     RT_TABLESTYLES},
    CT_TAGS: {  # ECMA-376-1 13.3.12
        'basename':    'tag',
        'ext':         '.xml',
        'name':        'User-Defined Tags Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/tags',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['presentation', 'slide'],
        'reltype':     RT_TAGS},
    CT_TEMPLATE: {  # ECMA-376-1 13.3.6
        # one of three possible Content Type values for presentation part
        'basename':    'presentation',
        'ext':         '.xml',
        'name':        'Presentation Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    True,
        'baseURI':     '/ppt',
        'has_rels':    PTS_HASRELS_ALWAYS,
        'rels_from':   ['package'],
        'reltype':     RT_TEMPLATE},
    CT_THEME: {  # ECMA-376-1 14.2.7
        'basename':    'theme',
        'ext':         '.xml',
        'name':        'Theme Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        # spec indicates theme part is optional, but I've never seen a .pptx
        # without one
        'required':    True,
        'baseURI':     '/ppt/theme',
        # can have _rels items, but only if theme contains one or more images
        'has_rels':    PTS_HASRELS_OPTIONAL,
        'rels_from':   ['presentation', 'handoutMaster', 'notesMaster',
                        'slideMaster'],
        'reltype':     RT_THEME},
    CT_VIEW_PROPS: {  # ECMA-376-1 13.3.13
        'basename':    'viewProps',
        'ext':         '.xml',
        'name':        'View Properties Part',
        'cardinality': PTS_CARDINALITY_SINGLETON,
        'required':    False,
        'baseURI':     '/ppt',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['presentation'],
        'reltype':     RT_VIEWPROPS},
    'image/gif': {  # ECMA-376-1 15.2.14
        'basename':    'image',
        'ext':         '.gif',
        'name':        'Image Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/media',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['handoutMaster', 'notesSlide', 'notesMaster', 'slide',
                        'slideLayout', 'slideMaster'],
        'reltype':     RT_IMAGE},
    'image/jpeg': {  # ECMA-376-1 15.2.14
        'basename':    'image',
        'ext':         '.jpeg',
        'name':        'Image Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/media',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['handoutMaster', 'notesSlide', 'notesMaster', 'slide',
                        'slideLayout', 'slideMaster'],
        'reltype':     RT_IMAGE},
    'image/png': {  # ECMA-376-1 15.2.14
        'basename':    'image',
        'ext':         '.png',
        'name':        'Image Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/media',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['handoutMaster', 'notesSlide', 'notesMaster', 'slide',
                        'slideLayout', 'slideMaster'],
        'reltype':     RT_IMAGE},
    'image/x-emf': {  # ECMA-376-1 15.2.14
        'basename':    'image',
        'ext':         '.emf',
        'name':        'Image Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/media',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   ['handoutMaster', 'notesSlide', 'notesMaster', 'slide',
                        'slideLayout', 'slideMaster'],
        'reltype':     RT_IMAGE
    },
    'image/vnd.ms-photo': {
        'basename':    'hdphoto',
        'ext':         '.wdp',
        'name':        'Image Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/media',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   [],
        'reltype':     RT_IMAGE
    },
    'image/tiff': {
        'basename':    'image',
        'ext':         '.tiff',
        'name':        'Image Part',
        'cardinality': PTS_CARDINALITY_TUPLE,
        'required':    False,
        'baseURI':     '/ppt/media',
        'has_rels':    PTS_HASRELS_NEVER,
        'rels_from':   [],
        'reltype':     RT_IMAGE
    }
}


# ============================================================================
# default_content_types
# ============================================================================
# Default file extension to MIME type mapping. This is used as a reference for
# adding <Default> elements to [Content_Types].xml for parts like media files.
#     TODO: I've seen .wmv elements in the media folder of at least one
# presentation, might need to add an entry for that and perhaps other rich
# media PowerPoint allows to be embedded (e.g. audio, movie, object, ...).
# ============================================================================

default_content_types = {
    '.bin':     CT_PRINTER_SETTINGS,
    '.emf':     'image/x-emf',
    '.fntdata': 'application/x-fontdata',
    '.gif':     'image/gif',
    '.jpe':     'image/jpeg',
    '.jpeg':    'image/jpeg',
    '.jpg':     'image/jpeg',
    '.png':     'image/png',
    '.rels':    'application/vnd.openxmlformats-package.relationships+xml',
    '.tif':     'image/tiff',
    '.tiff':    'image/tiff',
    '.wdp':     'image/vnd.ms-photo',
    '.wmf':     'image/x-wmf',
    '.xlsx':    CT_EXCEL_XLSX,
    '.xml':     'application/xml'}


# ============================================================================
# nsmap
# ============================================================================
# namespace prefix to namespace name map
# ============================================================================

nsmap = {
    'a':   'http://schemas.openxmlformats.org/drawingml/2006/main',
    'cp':  ('http://schemas.openxmlformats.org/package/2006/metadata/core-pro'
            'perties'),
    'ct':  'http://schemas.openxmlformats.org/package/2006/content-types',
    'dc':  'http://purl.org/dc/elements/1.1/',
    'dcmitype': 'http://purl.org/dc/dcmitype/',
    'dcterms':  'http://purl.org/dc/terms/',
    'ep':  ('http://schemas.openxmlformats.org/officeDocument/2006/extended-p'
            'roperties'),
    'i':   RT_IMAGE,
    'm':   'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'mo':  'http://schemas.microsoft.com/office/mac/office/2008/main',
    'mv':  'urn:schemas-microsoft-com:mac:vml',
    'o':   'urn:schemas-microsoft-com:office:office',
    'p':   'http://schemas.openxmlformats.org/presentationml/2006/main',
    'pd':  ('http://schemas.openxmlformats.org/drawingml/2006/presentationDra'
            'wing'),
    'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture',
    'pr':  'http://schemas.openxmlformats.org/package/2006/relationships',
    'r':   ('http://schemas.openxmlformats.org/officeDocument/2006/relationsh'
            'ips'),
    'sl':  ('http://schemas.openxmlformats.org/officeDocument/2006/relationsh'
            'ips/slideLayout'),
    'v':   'urn:schemas-microsoft-com:vml',
    've':  'http://schemas.openxmlformats.org/markup-compatibility/2006',
    'w':   'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'w10': 'urn:schemas-microsoft-com:office:word',
    'wne': 'http://schemas.microsoft.com/office/word/2006/wordml',
    'wp':  ('http://schemas.openxmlformats.org/drawingml/2006/wordprocessingD'
            'rawing'),
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'}


def namespaces(*prefixes):
    """
    Return a dict containing the subset namespace prefix mappings specified by
    *prefixes*. Any number of namespace prefixes can be supplied, e.g.
    namespaces('a', 'r', 'p').
    """
    namespaces = {}
    for prefix in prefixes:
        namespaces[prefix] = nsmap[prefix]
    return namespaces


def qtag(tag):
    """
    Return a qualified name (QName) for an XML element or attribute in Clark
    notation, e.g. ``'{http://www.w3.org/1999/xhtml}body'`` instead of
    ``'html:body'``, by looking up the specified namespace prefix in the
    overall namespace map (nsmap) above. Google on "xml clark notation" for
    more on Clark notation. *tag* is a namespace-prefixed tagname, e.g.
    ``'p:cSld'``.
    """
    prefix, tagroot = tag.split(':')
    uri = nsmap[prefix]
    return '{%s}%s' % (uri, tagroot)
