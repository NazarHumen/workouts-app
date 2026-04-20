from django.shortcuts import render, get_object_or_404, redirect
from workouts.forms import WorkoutForm, ExerciseFormSet
from workouts.models import Workout


def workout_list(request):
    workouts = Workout.objects.all().order_by('-date')
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})


def workout_create(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_add_exercises', pk=workout.pk)
    else:
        form = WorkoutForm()
    return render(request, 'workouts/workout_form.html', {
        'form': form,
    })


def workout_add_exercises(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if workout.completed:
        return redirect('workout_detail', pk=workout.pk)
        
    if request.method == 'POST':
        formset = ExerciseFormSet(request.POST, instance=workout)
        if formset.is_valid():
            formset.save()
            return redirect('workout_detail', pk=workout.pk)
    else:
        formset = ExerciseFormSet(instance=workout)
    return render(request, 'workouts/exercise_form.html', {
        'workout': workout,
        'formset': formset
    })


def workout_edit(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    if workout.completed:
        return redirect('workout_detail', pk=workout.pk)

    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_add_exercises', pk=workout.pk)
    else:
        form = WorkoutForm(instance=workout)
    return render(request, 'workouts/workout_form.html', {
        'form': form,
        'workout': workout,
        'is_edit': True
    })


def workout_detail(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    return render(request, 'workouts/workout_detail.html',
                  {'workout': workout})


def workout_complete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    workout.completed = True
    workout.save()
    return redirect('workout_detail', pk=pk)


def workout_delete(request, pk):
    workout = get_object_or_404(Workout, pk=pk)
    workout.delete()
    return redirect('workout_list')
