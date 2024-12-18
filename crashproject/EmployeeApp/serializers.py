from django.db.models import Sum
from rest_framework import serializers

from .models import Equipe, Employee, Tache, Competence, Department, EmployeeCompetence, Affectation, EmploymentHistory
from .models import Onboarding, EtapeOnboarding
from .models import Poste


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'




class PosteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poste
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = '__all__'


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competence
        fields = '__all__'



class OnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onboarding
        fields = ['id', 'nomCycle']

# serializers.py


class EtapeOnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapeOnboarding
        fields = ['id', 'numeroEtape', 'description', 'onboarding']


class EmployeeCompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCompetence
        fields = '__all__'





class AffectationSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.firstName', read_only=True)
    post_name = serializers.CharField(source='poste.nomPoste', read_only=True)

    class Meta:
        model = Affectation
        fields = ['employee', 'employee_name', 'poste', 'post_name', 'ratio']

    def validate(self, data):
        # Check if the employee already has affectations
        if Affectation.objects.filter(employee=data['employee']).exists():
            # Sum up existing ratios
            existing_ratios_sum = Affectation.objects.filter(employee=data['employee']).aggregate(Sum('ratio'))['ratio__sum'] or 0

            # Calculate the sum with the new ratio
            total_ratio_sum = existing_ratios_sum + data['ratio']

            # Check if the total ratio sum exceeds 100
            if total_ratio_sum > 100:
                raise serializers.ValidationError("The total ratio sum for the employee exceeds 100%.")

        return data

class EmploymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = ['employee', 'employer', 'position', 'start_date', 'end_date', 'responsibilities']



class EmployeeSearchSerializer(serializers.ModelSerializer):
    competences = serializers.StringRelatedField(many=True)

    class Meta:
        model = Employee
        fields = ['id', 'firstName', 'lastName', 'position', 'competences']




