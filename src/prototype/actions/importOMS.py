# -*- coding: utf-8 -*-

# Version 1403 Dgt  
from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as Xml


# Import the logger
import logging

#Import Database class
from prototype.models import  Model, Entity, Property, Relationship     
from protoLib.utilsConvert import toBoolean


class importOMS():

    def __init__(self):
        self.__filename = ""
        self.__tree = None
        self.__session = None

        # Manejo del log 
        self.__logger = logging.getLogger("Convert XML Database")
        self.__logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.__logger.addHandler(handler)
        
        
        # Errors Constants
        self.OK = 0
        self.ERROR_OPEN_FILE = 1
        self.ERR0R_PARSE_XML = 2
        self.OPERATIONAL_ERROR = 3
        self.ADDING_ERROR = 4
        self.ERROR = 5
        


    # filename doit etre un fichier XML
    def loadFile(self, filename):
        # In oder to conserve the file
        self.__tree = ElementTree()
        
        #Logging info
        self.__logger.info("Chargement du fichier...")
        
        #self.__tree.parse(filename)
        try:
            self.__tree.parse(filename)
            self.__filename = filename
            
        except IOError:
            self.__logger.critical("Impossible d ouvrir le fichier...")
            return self.ERROR_OPEN_FILE
        except:
            self.__logger.critical("Erreur de traitement fichier...")
            return self.ERROR
        
        #Logging info
        self.__logger.info("Chargement du fichier effectue...")
        
        return self.OK
    
        
    def __write(self):

        #Logging info
        self.__logger.info("Ecriture dans la base de donnee...")

        # Los elementos superXXX son referencias de tipo caracter,
        fdsModel= ( 'code', 'category',  'modelPrefix',  )
        
        fdsEntity= ( 'code',  )
        
        # fdsProperty = ( 'code', 'alias', 'physicalName', 'foreignEntity' )
        fdsProperty = ( 'code',  )
        booProperty = ( 'isPrimary', 'isNullable', 'isRequired', 'isSensitive', 'isEssential', )
        
        fdsRelationship = ( 'code', 'baseMin', 'baseMax', 'refMin', 'refMax', )


        # We populate the database
        if (self.__tree != None):  # A file has been loaded
        
            xProjects = self.__tree.getiterator("domain")
            
            # ------------------------------------------------------------------------------
            xModels = xProjects[0].getiterator("model")
            for xModel in xModels:
                dModel = Model()
                dModel.project = self.project 
                modelUdps = []

                for child in xModel:
                    if child.tag in fdsModel:
                        setattr( dModel, child.tag, child.text )
                    elif child.tag == 'udps':
                        for xUdp in child:
                            modelUdps.append( (xUdp.tag, xUdp.get('text') ) )

                try:
                    dModel.save()
                except:  
                    self.__logger.info("Error dModel.save")
                    return
                    
                if len( modelUdps ) > 0: 
                    self.saveModelUdps( modelUdps, dModel )
                
                self.__logger.info("Model..."  + dModel.code)

                # ------------------------------------------------------------------------------
                xEntitys = xModel.getiterator("concept")
                for xEntity in xEntitys:
                    dEntity = Entity()
                    dEntity.model = dModel
                    
                    for child in xEntity:
                        if (child.tag in fdsEntity):
                            if (child.text is not None):
                                setattr( dEntity, child.tag, child.text )
                        elif  ( child.tag == 'physicalName' ):
                            setattr( dEntity, 'dbName' , child.text )
                        
                    try:              
                        dEntity.save()
                    except: 
                        self.__logger.info("Error dEntity.save")
                        return

                    self.__logger.info("Entity..."  + dEntity.code)


                    # ------------------------------------------------------------------------------
                    xProperties = xEntity.getiterator("property")
                    for xProperty in xProperties:
                        
                        dProperty = Property()
                        dProperty.entity = dEntity

                        for child in xProperty:

                            if child.tag in fdsProperty:
                                if (child.text is not None):
                                    setattr( dProperty, child.tag, child.text )

#                             elif  ( child.tag == 'physicalName' ):
#                                 setattr( dProperty, 'dbName' , child.text )
                                
                            elif child.tag in booProperty:
                                bValue = toBoolean(child.text )
                                setattr( dProperty, child.tag, bValue )


                        try: 
                            dProperty.save()
                        except: 
                            self.__logger.info("Error prpDom.save")
                            return


                    # Relationship -------------------------------------------------------------------
                    xForeigns = xEntity.getiterator("foreign")
                    for xForeign in xForeigns:
                        dForeign = Relationship()
                        dForeign.entity  = dEntity 

                        dForeign.refEntity = dEntity

                        for child in xForeign:
                            if child.tag in fdsRelationship:
                                setattr( dForeign, child.tag, child.text)

                            elif  ( child.tag == 'baseConcept' ):
                                setattr( dForeign, 'dbName' , child.text )

                            elif  ( child.tag == 'alias' ):
                                setattr( dForeign, 'relatedName' , child.text )
                                
                            elif child.tag in booProperty:
                                bValue = toBoolean(child.text )
                                setattr( dForeign, child.tag, bValue )

                        try:
                            dForeign.save()
                        except Exception, e: 
                            self.__logger.info("Error dForeign.save"  + str(e))
                            return


            # Recorre las llaves para asociar los FK 
            for dForeign in Relationship.objects.all(): 
                pass 

        
        #Logging info
        self.__logger.info("Ecriture dans la base de donnee effectuee...")
        return {'state':self.OK, 'message': 'Ecriture effectuee'}
    
        
    def doImport(self, dProject ): 
        # We write in the database
    
        self.project = dProject 
    
        dictWrite = self.__write()
        if (dictWrite['state'] != self.OK):
            return dictWrite
                
        return {'state':self.OK, 'message': 'Ecriture effectuee base donnee'}
    
    
    def saveModelUdps(self, udps, dModel ):
        for key, value  in udps:
#             dUdp = UdpModel()
#             dUdp.model = dModel
#             dUdp.code = key
#             dUdp.valueUdp = value
#             dUdp.save()
            pass

    def savePrpUdps(self, udps, dPrp ):
        for key, value  in udps:
            pass


    def getEntityRef( self, dModel , cName  ):
        mAux = Entity.objects.filter( model = dModel, code = cName  )
        if mAux: 
            return mAux[0] 


        
        
    #RETOUR : le nom d un fichier XML
    def getFilename(self):
        return self.__filename
    
    # Transform XML Element  to text
    def getContentFile(self):
        
        #Logging info
        self.__logger.info("Obtention du contenu du fichier...")
        
        contenu = None
        if (self.__tree == None):
            contenu = ""
        else:
            contenu = Xml.tostring(self.__tree.getroot())
            
        #Logging info
        self.__logger.info("Obtention du contenu du fichier effectuee...")    
        return contenu



def definePropertyList():
#    Obtiene la lista de propiedades  
#        fdsProject = [field.name for field in Project._meta.fields]
#        fdsModel= [field.name for field in Model._meta.fields]
#        fdsEntity= [field.name for field in Entity._meta.fields]
#        fdsProperty= [field.name for field in Property._meta.fields]
#        fdsForeign= [field.name for field in Relationship._meta.fields]
    
    pass
    