from prototype.models import *

def createTestProject():

    projectdata = {
        'code': 'testCode',
        'description': 'Project used for tests',
        'dbEngine': 'MySQL',
        'dbName': 'testDatabase',
        'dbUser': 'testdbUser',
        'dbPassword': 'testdbPassword',
        'dbHost': 'testlocalhost',
        'dbPort': 'testPort'
    }

    testProject = Project(**projectdata)
    testProject.save()

    return testProject


def createTestModel():
    testProject = createTestProject()
    testProject.save()

    modeldata = {
        'project': testProject,
        'code': 'testCode',
        'category': 'testCategory',
        'modelPrefix': 'testPrefix',
        'description': 'Model used for tests'
    }

    testModel = Model(**modeldata)
    testModel.save()

    return testModel


def createTestEntity():
    testModel = createTestModel()
    testModel.save()

    entitydata = {
        'model': testModel,
        'code': 'testEntityCode',
        'dbName': 'testEntitydbName',
        'description': 'testEntityDescription'
    }

    testEntity = Entity(**entitydata)
    testEntity.save()

    return testEntity



def createTestProperty():
    testEntity = createTestEntity()
    testEntity.save()


    propertydata = {
        'entity': testEntity,
        'isPrimary': True,
        'isLookUpResult': True,
        'isNullable': True,
        'isRequired': True,
        'isReadOnly': True,
        'isEssential': True,
        'isForeign': False,
        'isSensitive' : True,
        'crudType': 'testCrudType',
        'dbName': 'testDbName'
    }

    testProperty = Property(**propertydata)
    testProperty.save()

    return testProperty


def createTestRelationship():
    testEntity1 = createTestEntity()
    testEntity1.save()

    testEntity2 = createTestEntity()
    testEntity2.save()


    relationshipdata = {
        'refEntity': testEntity1,
        'baseMin': 'testBaseMin',
        'baseMax': 'testBaseMax',
        'refMin': 'testRefMin',
        'refMax': 'testRefMax',
        'onRefDelete': 'testOnRefDelete',
        'typeRelation': 'testTypeRelation',

        'entity': testEntity2,
        'isPrimary': True,
        'isLookUpResult': True,
        'isNullable': True,
        'isRequired': True,
        'isReadOnly': True,
        'isEssential': True,
        'isForeign': False,
        'isSensitive' : False,
        'crudType': 'testCrudType',
        'dbName': 'testDbName'
    }

    testRelationShip = Relationship(**relationshipdata)
    testRelationShip.save()

    return testRelationShip


def createTestPropertyEquivalence():
    testProperty1 = createTestProperty()
    testProperty1.save()
    testProperty2 = createTestProperty()
    testProperty2.save()

    propertyequivalencedata = {
        'sourceProperty': testProperty1,
        'targetProperty': testProperty2,
        'description': 'testDescription'
    }

    testPropertyEquivalence = PropertyEquivalence(**propertyequivalencedata)
    testPropertyEquivalence.save()

    return testPropertyEquivalence


def createTestPrototype():
    testEntity = createTestEntity()
    testEntity.save()

    prototypedata = {
        'entity': testEntity,
        'code': 'testCode',
        'description': 'testDescription',
        'notes': 'testNotes',
        'metaDefinition': 'testMetaDefinition'
    }

    testPrototype = Prototype(**prototypedata)
    testPrototype.save()

    return testPrototype


def createTestDiagram():
    testModel = createTestModel()
    testModel.save()

    diagramdata = {
        'model': testModel,
        'code': 'testCode',
        'description': 'testDescription',
        'notes': 'testNotes'
    }

    testDiagram = Diagram(**diagramdata)
    testDiagram.save()

    return testDiagram


def createTestDiagramEntity():
    testDiagram = createTestDiagram()
    testDiagram.save()

    testEntity = createTestEntity()
    testEntity.save()

    diagramentitydata = {
        'diagram': testDiagram,
        'entity': testEntity
    }

    testDiagramEntity = DiagramEntity(**diagramentitydata)
    testDiagramEntity.save()

    return testDiagramEntity


def createTestService():
    testModel = createTestModel()
    testModel.save()

    servicedata = {
        'model': testModel,
        'code': 'testCode',
        'Binding': 'testBinding',
        'typeMessage': 'testMessage',
        'description': 'testDescription',
        'notes': 'testNotes'
    }

    testService = Service(**servicedata)
    testService.save()

    return testService


def createTestServiceRef():
    testModel = createTestModel()
    testModel.save()

    testService = createTestService()
    testService.save()

    servicerefdata = {
        'model': testModel,
        'service': testService,
        'endpoint': 'testEndPoint',
        'description': 'testDescription',
        'notes': 'testNotes'
    }

    testServiceRef = ServiceRef(**servicerefdata)
    testServiceRef.save()

    return testServiceRef


def createTestProtoTable():
    testEntity = createTestEntity()
    testEntity.save()

    prototabledata = {
        'entity': testEntity
    }

    testProtoTable = ProtoTable(**prototabledata)
    testProtoTable.save()

    return testProtoTable