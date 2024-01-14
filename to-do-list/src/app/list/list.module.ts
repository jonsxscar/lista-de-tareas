import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TareaListaComponent } from '../tarea-lista/tarea-lista.component';

@NgModule({
  declarations: [TareaListaComponent],
  imports: [CommonModule],
  exports: [TareaListaComponent]
})
export class TareaListaModule { }