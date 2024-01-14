import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';


interface Tarea {
  id: number;
  title: string;
  description: string;
  completed: boolean;
  date: string;
}

@Component({
  selector: 'tarea-lista',
  templateUrl: './tarea-lista.component.html',
  styleUrls: ['./tarea-lista.component.css']
})
export class TareaListaComponent {
  tareas: Tarea[] = [];
  nuevaTarea: Tarea = { id: 0, title: '', description: '', completed: false, date: '' };

  constructor(private http: HttpClient) {
    this.getTareas();
  }

  getTareas() {
    this.http.get<Tarea[]>('http://127.0.0.1:8000/api/tasks/').subscribe(tasks => {
      this.tareas = tasks;
    });
  }

  agregarTarea() {
    if (this.nuevaTarea.title && this.nuevaTarea.description) {
      this.http.post<Tarea>('http://127.0.0.1:8000/api/tasks/', this.nuevaTarea).subscribe(res => {
        // Agregar la tarea a la lista de tareas
        this.tareas.push(res);
        // Reiniciar la nuevaTarea
        this.nuevaTarea = { id: 0, title: '', description: '', completed: false, date: '' };
      });
    }
  }

  eliminarTarea(index: number) {
    const tarea = this.tareas[index];
    this.http.delete(`http://127.0.0.1:8000/api/tasks/${tarea?.id}`).subscribe(res => {
      // Eliminar la tarea de la lista de tareas
      this.tareas.splice(index, 1);
    });
  }

  updateNuevaTarea(field: keyof Tarea, event: Event) {
    if (this.nuevaTarea) {
      if (field === 'title' || field === 'description') {
        const target = event.target as HTMLInputElement;
        this.nuevaTarea[field] = target.value;
      }
    }
  }
}